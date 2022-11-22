from django.db import models

from deep_translator import GoogleTranslator

langs = [
	'en', 'ru', 'ar', 'fa'
]

# Create your models here.
class TextBlock(models.Model):
	# to call
	title = models.CharField(max_length=70, unique=True)

	def save(self, *args, **kwargs):
		self.title = self.title.replace(' ', '_').replace(',', '').replace('.', '').replace('-','_')
		super().save()

	def __str__(self):
		return self.title


class Text(models.Model):
	# to call
	related = models.ForeignKey(TextBlock, on_delete=models.CASCADE, related_name='texts')

	# base
	language = models.CharField(max_length=2)
	text = models.TextField(unique=True)

	# for translations
	source = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.language}_{self.related}'

	def save(self, *args, **kwargs):
		# translation:
		if self.source:	

			print('translating myself')
			success = False
			for lang in langs:
			
				if not lang == self.language:
					try:
						# translating
						trsl = GoogleTranslator(source=self.language, target=lang, timeout=5).translate
						translated = trsl(self.text)
						success = True
					except:
						print('could not translate')
	
				if success:
					# saving
					Text(
						related=self.related,
						language=lang,
						text=translated
					).save()
			if success:
				self.source = False

		super().save(*args, kwargs)


class FeedBackRequest(models.Model):
	from_page = models.CharField(max_length=20, null=True, blank=True)

	email = models.EmailField()
	name = models.CharField(max_length=32, null=False)
	phone = models.CharField(null=False, max_length=14)

	additional_message = models.TextField()

	done = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('created', )

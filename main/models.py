from django.db import models

# from deep_translator import GoogleTranslator

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


COUNTRY_CHOICES = [('Afghanistan', 'afghanistan'), ('Albania', 'albania'), ('Algeria', 'algeria'), ('Angola', 'angola'), ('Andorra', 'andorra'), ('Antigua and Barbuda', 'antigua and barbuda'), ('Armenia', 'armenia'), ('Argentina', 'argentina'), ('Australia', 'australia'), ('Bangladesh', 'bangladesh'), ('Austria', 'austria'), ('Bahrain', 'bahrain'), ('Azerbaijan', 'azerbaijan'), ('Bahamas', 'bahamas'), ('Barbados', 'barbados'), ('Belarus', 'belarus'), ('Benin', 'benin'), ('Belgium', 'belgium'), ('Belize', 'belize'), ('Bhutan', 'bhutan'), ('Bolivia', 'bolivia'), ('Bosnia and Herzegovina', 'bosnia and herzegovina'), ('Botswana', 'botswana'), ('Brazil', 'brazil'), ('Brunei', 'brunei'),('Bulgaria', 'bulgaria'), ('Burkina Faso', 'burkina faso'), ('Burundi', 'burundi'), ("Côte d'Ivoire", "côte d'ivoire"), ('Cabo Verde', 'cabo verde'), ('Cambodia', 'cambodia'), ('Cameroon', 'cameroon'), ('Canada', 'canada'), ('Central African Republic', 'central african republic'), ('Chad', 'chad'), ('Chile', 'chile'), ('China', 'china'), ('Colombia', 'colombia'), ('Comoros', 'comoros'), ('Congo (Congo-Brazzaville)', 'congo (congo-brazzaville)'), ('Costa Rica', 'costa rica'), ('Croatia', 'croatia'),('Cuba', 'cuba'), ('Cyprus', 'cyprus'), ('Czechia (Czech Republic)', 'czechia (czech republic)'), ('Democratic Republic of the Congo', 'democratic republic of the congo'), ('Denmark', 'denmark'), ('Djibouti', 'djibouti'), ('Dominica', 'dominica'), ('Dominican Republic', 'dominican republic'), ('Ecuador', 'ecuador'), ('Egypt', 'egypt'), ('El Salvador', 'el salvador'), ('Equatorial Guinea', 'equatorial guinea'), ('Eritrea', 'eritrea'), ('Estonia', 'estonia'), ('Eswatini (fmr. "Swaziland")', 'eswatini(fmr. "swaziland")'), ('Ethiopia', 'ethiopia'), ('Fiji', 'fiji'), ('Finland', 'finland'), ('France', 'france'), ('Gabon', 'gabon'), ('Gambia', 'gambia'), ('Georgia', 'georgia'), ('Germany', 'germany'), ('Ghana', 'ghana'), ('Greece', 'greece'), ('Grenada', 'grenada'), ('Guatemala', 'guatemala'), ('Guinea', 'guinea'), ('Guinea-Bissau','guinea-bissau'), ('Guyana', 'guyana'), ('Haiti', 'haiti'), ('Holy See', 'holy see'), ('Honduras', 'honduras'), ('Hungary', 'hungary'), ('Iceland', 'iceland'), ('India', 'india'), ('Indonesia', 'indonesia'), ('Iran', 'iran'), ('Iraq', 'iraq'), ('Ireland', 'ireland'), ('Israel', 'israel'), ('Italy', 'italy'), ('Jamaica', 'jamaica'), ('Japan', 'japan'), ('Jordan', 'jordan'), ('Kazakhstan', 'kazakhstan'), ('Kenya', 'kenya'), ('Kiribati', 'kiribati'), ('Kuwait', 'kuwait'), ('Kyrgyzstan', 'kyrgyzstan'),('Laos', 'laos'), ('Latvia', 'latvia'), ('Lebanon', 'lebanon'), ('Lesotho', 'lesotho'), ('Liberia', 'liberia'), ('Libya', 'libya'), ('Liechtenstein', 'liechtenstein'),('Lithuania', 'lithuania'), ('Luxembourg', 'luxembourg'), ('Madagascar', 'madagascar'), ('Malawi', 'malawi'), ('Malaysia', 'malaysia'), ('Maldives', 'maldives'), ('Mali', 'mali'), ('Malta', 'malta'), ('Marshall Islands', 'marshall islands'), ('Mauritania', 'mauritania'), ('Mauritius', 'mauritius'), ('Mexico', 'mexico'), ('Micronesia', 'micronesia'), ('Moldova', 'moldova'), ('Monaco', 'monaco'), ('Mongolia', 'mongolia'), ('Montenegro', 'montenegro'), ('Morocco', 'morocco'), ('Mozambique', 'mozambique'), ('Myanmar (formerly Burma)', 'myanmar (formerly burma)'), ('Namibia', 'namibia'), ('Nauru', 'nauru'), ('Nepal', 'nepal'), ('Netherlands', 'netherlands'), ('New Zealand', 'new zealand'), ('Nicaragua', 'nicaragua'), ('Niger', 'niger'), ('Nigeria', 'nigeria'), ('North Korea', 'north korea'), ('North Macedonia', 'north macedonia'), ('Norway', 'norway'), ('Oman', 'oman'), ('Pakistan', 'pakistan'), ('Palau', 'palau'), ('Palestine State', 'palestine state'), ('Panama', 'panama'), ('Papua New Guinea', 'papua new guinea'), ('Paraguay', 'paraguay'), ('Peru', 'peru'), ('Philippines', 'philippines'), ('Poland', 'poland'), ('Portugal', 'portugal'), ('Qatar', 'qatar'), ('Romania', 'romania'), ('Russia', 'russia'), ('Rwanda', 'rwanda'), ('Saint Kitts and Nevis', 'saint kitts and nevis'), ('Saint Lucia', 'saint lucia'), ('Saint Vincent andthe Grenadines', 'saint vincent and the grenadines'), ('Samoa', 'samoa'), ('San Marino', 'san marino'), ('Sao Tome and Principe', 'sao tome and principe'), ('Saudi Arabia', 'saudi arabia'), ('Senegal', 'senegal'), ('Serbia', 'serbia'), ('Seychelles', 'seychelles'), ('Sierra Leone', 'sierra leone'), ('Singapore', 'singapore'), ('Slovakia', 'slovakia'), ('Slovenia', 'slovenia'), ('Solomon Islands', 'solomon islands'), ('Somalia', 'somalia'), ('South Africa', 'south africa'), ('South Korea', 'south korea'), ('South Sudan', 'south sudan'), ('Spain', 'spain'), ('Sri Lanka', 'sri lanka'), ('Sudan', 'sudan'), ('Suriname', 'suriname'), ('Sweden', 'sweden'), ('Switzerland', 'switzerland'), ('Syria', 'syria'), ('Tajikistan', 'tajikistan'), ('Tanzania', 'tanzania'), ('Thailand', 'thailand'), ('Timor-Leste', 'timor-leste'), ('Togo', 'togo'), ('Tonga', 'tonga'), ('Trinidad and Tobago', 'trinidad and tobago'), ('Tunisia', 'tunisia'), ('Turkey', 'turkey'), ('Turkmenistan', 'turkmenistan'), ('Tuvalu', 'tuvalu'), ('Uganda', 'uganda'), ('Ukraine', 'ukraine'), ('United Arab Emirates', 'united arab emirates'), ('United Kingdom', 'united kingdom'), ('United States of America', 'united states of america'), ('Uruguay', 'uruguay'), ('Uzbekistan', 'uzbekistan'), ('Vanuatu', 'vanuatu'), ('Venezuela', 'venezuela'), ('Vietnam', 'vietnam'), ('Yemen','yemen'), ('Zambia', 'zambia'), ('Zimbabwe', 'zimbabwe')]
VISA_DURATION_CHOICES = [
	('Tourist visa(30 days)', 'Tourist visa(30 days)'), 
	('Tourist visa(60 days)', 'Tourist visa(60 days)'), 
	('Multivisa(30 days)', 'Multivisa(30 days)'),
	('Multivisa(60 days)', 'Multivisa(60 days)'),
	]


class DubaiVisaRequest(models.Model):
	passport_registered_at = models.CharField(max_length=200, choices=COUNTRY_CHOICES)
	now_located_in = models.CharField(max_length=200, choices=COUNTRY_CHOICES)

	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)

	visa_duration = models.CharField(max_length=120, choices=VISA_DURATION_CHOICES, default='Tourist visa(30 days)')

	passport_series = models.PositiveBigIntegerField()
	passport_open_date = models.DateField()
	passport_closure_date = models.DateField()

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	contact_information = models.TextField()

	class Meta:
		ordering = ('-created', )

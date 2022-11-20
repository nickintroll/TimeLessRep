from django.shortcuts import render, redirect
from .models import TextBlock


def get_texts(lang):
	texts = {}
	
	for block in TextBlock.objects.all():

		try:
			texts[block.title] = block.texts.filter(language=lang)[0]

		except IndexError:
			print('Missing text for "', block.title, '" for ', lang)

	return {'texts': texts}


def _render(req, template, context={}):

	lang = 'en'

	if 'lang' in req.COOKIES:
		# print('lang ha beed set before: ', req.COOKIES['lang'])

		context['texts'] = get_texts(req.COOKIES['lang'])

		return render(req, template, context)

	else:
		# print('Settings default lang to', lang)

		context['texts'] = get_texts(lang)
		ret = render(req, template, context)
		ret.set_cookie('lang', lang)

		return ret


# working part(all that lower)
def main_page(request):
	return _render(request, 'main/main_page.html')


# citizenship
def citi_romanian_eng(request):
	return _render(request, 'sub/citizenship/romania_eng.html')

def citi_bolgar_eng(request):
	return _render(request, 'sub/citizenship/bolgar_eng.html')

# resident card
def resident_moldavia(request):
	return _render(request, 'sub/resident/moldavia_eng.html')

# work visa
def workvisa_poland(request):
	return _render(request, 'sub/work_visa/poland_eng.html')

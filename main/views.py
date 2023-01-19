from django.shortcuts import render, redirect
from .models import TextBlock
from .forms import RequestForm


def get_texts(lang):
	texts = {}
	
	for block in TextBlock.objects.all():
		try:
			texts[block.title] = block.texts.filter(language=lang)[0]
		except IndexError:
			print('Missing text for "', block.title, '" for ', lang)

	return {'texts': texts}


def _render(req, template, context={}, from_page='any'):

	lang = 'en'

	if 'lang' in req.COOKIES:
# 		print('lang ha beed set before: ', req.COOKIES['lang'])

		# save request
		if req.method == 'POST':
			form = RequestForm(req.POST)
			
			if form.is_valid():
			
				db_req = form.save(commit=False)
				db_req.from_page = from_page
				db_req.save()

		context['req_form'] = RequestForm
		context['texts'] = get_texts(req.COOKIES['lang'])

		return render(req, template, context)

	else:
# 		print('Settings default lang to', lang)
		context['req_form'] = RequestForm
		context['texts'] = get_texts(lang)


		ret = render(req, template, context)
		ret.set_cookie('lang', lang)

		return ret


# working part(all that lower)
def main_page(request):
	return _render(request, 'main/main_page.html', from_page='main page')

# citizenship
def citi_romanian_eng(request):
	return _render(request, 'sub/citizenship/romania_eng.html', from_page='citizenship for romania')

def citi_bolgar_eng(request):
	return _render(request, 'sub/citizenship/bolgar_eng.html', from_page='citizenship for bolgaria')

# resident card
def resident_moldavia(request):
	return _render(request, 'sub/resident/moldavia_eng.html', from_page='resident card for moldovia')

# work visa
def workvisa_poland(request):
	return _render(request, 'sub/work_visa/poland_eng.html', from_page='workvisa for poland')

def workvisa_vengria(request):
	# created in 1 month
	# works for 1 year
	return _render(request, 'sub/work_visa/vengria.html', from_page='workvisa for vengria')

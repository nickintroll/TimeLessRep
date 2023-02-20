from django.shortcuts import render, redirect
from django.urls import reverse

from aiogram import Bot
from asyncio import run as asyncrun
from time import sleep

from .models import TextBlock, DubaiVisaRequest
from .forms import RequestForm, DubaiVisaRequestForm, RequestSearchForm


def get_texts(lang):
	texts = {}
	
	for block in TextBlock.objects.all():
		try:
			texts[block.title] = block.texts.filter(language=lang)[0]
		except IndexError:
			print('Missing text for "', block.title, '" for ', lang)

	return {'texts': texts}


def _render(req, template, context={}, from_page='any', req_form=True):
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

		context['texts'] = get_texts(req.COOKIES['lang'])

		req = render(req, template, context)

	else:
# 		print('Settings default lang to', lang)
		context['texts'] = get_texts(lang)


		req = render(req, template, context)
		req.set_cookie('lang', lang)

	context['req_form'] = RequestForm	

	if req_form != True:
		del context['req_form']

	return req

def find_request(request):
	message = None
	result = None

	form = RequestSearchForm(request.GET)
	if form.is_valid():
		cd = form.cleaned_data
		if len([i for i in cd['request'].replace(' ', '') if not i.isdigit()]):
			print('wrong request')
		else:
			try:
				result = DubaiVisaRequest.objects.get(passport_series=cd['request'].replace(' ', ''))
			except DubaiVisaRequest.DoesNotExist:
				message = 'Did not find anyting for that request'



	return _render(request, 'main/request_get.html', context={'form': form, 'message': message, 'result': result}) 

async def bot_notify(bot, chat, message):
	await bot.send_message(chat, message)


def dubai_main_page(request):
	note = None
	form = DubaiVisaRequestForm()
	if request.method == 'GET':
		note = None

	if request.method == 'POST':
		form = DubaiVisaRequestForm(request.POST)
	
		if form.is_valid():

			form.save()
			note = 'Your request is saved, here you can check it\'s status, '
			bot = Bot('6184370515:AAFifYARgWR6PzickGu-FLR5vQjSEdopz0w')

			admins = [1751516505, 1941865554]
			for ad in admins:
				try:
					asyncrun(
						bot_notify(
							bot, 
							ad, 
							'New dubai request! \nCheck https://proglobalwork.com/controller_admin_page/ \n\n login: admin\npassword: ne12wpa41ss5352wor234dJustForUsToUSe'
							)
						)
					sleep(0.5)
					print('sent notify')
				except:
					print('did not send notification to ', ad)

		else:
			print(form.errors)
	return _render(request, 'main/dubai_main.html', context={'form': form, 'note':note})


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

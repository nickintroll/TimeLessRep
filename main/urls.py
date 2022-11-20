from django.urls import path
from .views import main_page, citi_romanian_eng, citi_bolgar_eng, resident_moldavia, workvisa_poland


app_name = 'main'
urlpatterns = [
	path('', main_page, name='main_page'),

	# citizenships
	path('citizen/romania/eng/', citi_romanian_eng, name='citi_roman_eng'),
	path('citizen/bolgar/eng/', citi_bolgar_eng, name='citi_bolgar_eng'),

	# resident card
	path('resident/moldavia/eng/', resident_moldavia, name='resident_moldavia_eng'),

	# work visa
	path('work_visa/poland/eng/', workvisa_poland, name='workvisa_poland_eng')
]
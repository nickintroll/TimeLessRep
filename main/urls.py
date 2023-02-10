from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.dubai_main_page, name='main_page'),
	path('travel/', views.main_page, name='host_page'),
	# get request dubai
	path('get_my_request/', views.find_request, name='my_requests'),


	# citizenships
	path('citizen/romania/', views.citi_romanian_eng, name='citi_roman_eng'),
	path('citizen/bolgar/', views.citi_bolgar_eng, name='citi_bolgar_eng'),

	# resident card
	path('resident/moldavia/', views.resident_moldavia, name='resident_moldavia_eng'),

	# work visa
	path('work_visa/poland/', views.workvisa_poland, name='workvisa_poland_eng'),
	path('work_visa/vengria/', views.workvisa_vengria, name='workvisa_vengria'),

]
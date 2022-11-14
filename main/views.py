from django.shortcuts import render

def main_page(request):
	# main page
	return render(request, 'sub/main_page.html')
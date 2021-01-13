from django.shortcuts import render

def portfolio(request):
	return render(request,'portfolio.html')

def about(request):
	return render(request,'about.html')

def projects(request):
	return render(request, 'projects.html')

def contacts(request):
	return render(request, 'contacts.html')

def flexbox(request):
	return render(request, 'flexbox.html')

def calculator(request):
	return render(request, 'calculator.html')

def website(request):
	return render(request, 'website.html')

def flexboxadvance(request):
	return render(request, 'flexboxadvance.html')

def SQL(request):
	return render(request, 'SQL.html')

def video(request):
	return render(request, 'video.html')


from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def search(request):
	if request.method == 'POST':
		search = request.POST['search']
	return render(request, 'search.html')

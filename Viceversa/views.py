from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
	return render(request, 'page1.html')
pass

def reverse(request):
	user_text = request.GET['usertext'][::-1]
	return render(request, 'reversed text.html', {'usertext': user_text})
pass

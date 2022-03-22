from django.http import HttpResponse
from django.shortcuts import render

def page1(request):
	return render(request, 'page1.html')
pass

def reverse(request):
	user_text = request.GET['usertext']
	reverse_text =user_text[::-1]
	words_count = len(user_text.split())
	return render(request, 'reversed text.html', {'usertext': user_text, 'reversetext': reverse_text,\
		'wordscount':words_count})
pass

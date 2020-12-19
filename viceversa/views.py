from django.shortcuts import render

def home (request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	list_of_user_text = user_text.split()
	lenwords_of_user_text = len(list_of_user_text)
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reversed_text, 'lenwords':lenwords_of_user_text})
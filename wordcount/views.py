from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	textarea_text = request.GET['fulltext']
	split_textarea_text = textarea_text.split()

	word_dictionary = {}

	for word in split_textarea_text:
		if word in word_dictionary:
			word_dictionary[word] += 1
		else:
			word_dictionary[word] = 1

	sorted_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'full_text':textarea_text, 'total_words':len(split_textarea_text), 
		'sorted_list':sorted_list})
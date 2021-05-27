from django.shortcuts import render
from .models import Blog
# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def result(request):
    sentence = request.GET['sentence']

    teamList = sentence.split(',')
    
    return render(request, 'result.html', {'fulltext':sentence, 'count':len(teamList), 'teamList':teamList})
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    questions = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}',
            'grade': i,
            'answers': f'Answers({i})',
            'first_tag': f'first tag {i}',
            'second_tag': f'second tag {i}'
        } for i in range(10)
    ]
    return render(request, 'index.html', {'questions': questions})

def question(request):
    return render(request, 'question.html')

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def settings(request):
    return render(request, 'settings.html')

def signup(request):
    return render(request, 'signup.html')
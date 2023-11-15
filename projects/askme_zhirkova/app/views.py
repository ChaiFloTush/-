from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator

QUESTIONS = [
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

ANSWERS = [
        {
            'id': i,
            'content': f'Long lorem ipsum {i}',
            'grade': i,
        } for i in range(10)
    ]

def paginate(objects, page, per_page=5):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page), 'page': page})

def question(request, question_id):
    item = QUESTIONS[question_id]
    page = request.GET.get('page', 1)
    return render(request, 'question.html', {'question': item, 'answers':paginate(ANSWERS, page), 'page': page})

def ask(request):
    return render(request, 'ask.html')

def login(request):
    return render(request, 'login.html')

def settings(request):
    return render(request, 'settings.html')

def signup(request):
    return render(request, 'signup.html')
from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator

from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

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

TAGS = [
    {
        'id': i,
        'name': f'Tag#{i}',
    } for i in range(7)
]

def paginate(objects, request, per_page=5):
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page', 1)
    try:
        return paginator.page(page)
    except EmptyPage:
        return paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        return paginator.page(1)

# Create your views here.
def index(request):
    return render(request, 'index.html', {'tags':TAGS, 'questions': paginate(QUESTIONS, request), 'page': paginate(QUESTIONS, request)})

def hot(request):
    return render(request, 'hot.html', {'tags':TAGS,'questions': paginate(QUESTIONS, request), 'page': paginate(QUESTIONS, request)})

def tag(request, popular_tag):
    return render(request, 'tag.html', {'tags':TAGS,'popular_tag': popular_tag, 'questions': paginate(QUESTIONS, request), 'page': paginate(QUESTIONS, request)})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html', {'tags':TAGS,'question': item, 'answers':paginate(ANSWERS, request), 'page': paginate(QUESTIONS, request)})

def ask(request):
    return render(request, 'ask.html', {'tags':TAGS})

def login(request):
    return render(request, 'login.html', {'tags':TAGS})

def settings(request):
    return render(request, 'settings.html', {'tags':TAGS})

def signup(request):
    return render(request, 'signup.html', {'tags':TAGS})
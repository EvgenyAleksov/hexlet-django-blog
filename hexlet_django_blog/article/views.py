from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

tags = [
    {'article_id': 1, 'tag': 'Обучение'},
    {'article_id': 2, 'tag': 'Программирование'},
    {'article_id': 3, 'tag': 'python'},
    {'article_id': 4, 'tag': 'OOP'},
]


def index(request, tags=None, article_id=None):
    tags = 'python'
    article_id = 42

    return render(request, 'articles/index.html',
        context={'article_id': article_id, 'tags': tags})


# def index(request):
#    return render(
#    request,
#    'articles/index.html',
#    context={'tags': tags},
#    )

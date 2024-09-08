from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

tags = [
    {'article_id': 1, 'tag': 'Обучение'},
    {'article_id': 2, 'tag': 'Программирование'},
    {'article_id': 3, 'tag': 'Python'},
    {'article_id': 4, 'tag': 'OOP'},
]

def index(request):
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )


# def index(request):
#    return HttpResponse('article')


# class HomePageView(View):

#    template_name = "index.html"
    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context
    
from django.urls import path
from hexlet_django_blog.article import views
# from hexlet_django_blog.article.views import HomePageView

urlpatterns = [
    path('', views.index), # <- добавляем эту строчку
]


# urlpatterns = [
#    path('', HomePageView.as_view()),
# ]
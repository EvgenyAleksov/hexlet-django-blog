from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]

# urlpatterns = [
#    path('', views.index),
# ]

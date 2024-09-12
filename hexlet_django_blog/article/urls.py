from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.index),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
]

# urlpatterns = [
#    path('', views.index),
# ]

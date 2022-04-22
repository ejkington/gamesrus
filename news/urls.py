from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsList.as_view(), name='news'),
    path('<slug:slug>/', views.NewsDetail.as_view(), name='news_detail'),
]

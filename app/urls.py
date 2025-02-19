from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryListCreateAPIView.as_view()),
]
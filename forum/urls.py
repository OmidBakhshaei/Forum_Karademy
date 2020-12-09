# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.urls import path
from .views import QuestionDetailView, CategoryDetailView
from . import views

urlpatterns = [
    # path('', HomeView.as_view(), name="forum-home"),
    path('', views.home, name="forum-home"),
    path('questions/', views.questions, name="questions"),
    path('questions/ask/', views.ask, name="questions-ask"),
    path('categories/', views.categories, name="categories"),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name="category_details"),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name="question_details"),
]

# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.urls import path
from .views import (
    HomeListView,
    AskQuestionCreateView,
    QuestionsListView,
    QuestionDetailView,
    QuetsionUpdateView,
    QuestionDeleteView,
    CategoriesListView,
    CategoryDetailView,
    like_view,
)
# from . import views

urlpatterns = [
    # path('', HomeView.as_view(), name="forum-home"),
    path('', HomeListView.as_view(), name="forum-home"),
    path('questions/', QuestionsListView.as_view(), name="questions"),
    path('questions/ask/', AskQuestionCreateView.as_view(), name="questions_ask"),
    path('categories/', CategoriesListView.as_view(), name="categories"),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name="category_details"),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name="question_details"),
    path('questions/<int:pk>/edit/', QuetsionUpdateView.as_view(), name="question_update"),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name="question_delete"),
    path('like/<int:pk>/', like_view, name="question_like"),
]

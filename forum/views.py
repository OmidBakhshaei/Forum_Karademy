# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Answer, Category


# class HomeView(ListView):
#     model = Question
#     template_name = 'forum/home.html'
def home(request):
    context = {
        'questions': Question.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'forum/home.html', context)


def questions(request):
    return render(request, 'forum/questions.html')


def ask(request):
    return render(request, 'forum/ask.html')


def categories(request):
    context = {
        'questions': Question.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'forum/categories.html', context)


# def question_details(request):
#     return render(request, 'forum/question_details.html')

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_details.html'
    # return render(request, 'forum/question_details.html')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'forum/category_details.html'
    # return render(request, 'forum/question_details.html')

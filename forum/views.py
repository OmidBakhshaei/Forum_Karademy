# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer, Category
from .forms import QuestionForm

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
    context = {
        'questions': Question.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'forum/questions.html', context)


# def ask(request):
#     return render(request, 'forum/ask.html')
class AskQuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'forum/ask.html'
    # fields = ['title', 'question', 'questioner', 'category', 'answered']


def categories(request):
    context = {
        'questions': Question.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'forum/categories.html', context)



class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_details.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'forum/category_details.html'

# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Category
from .forms import QuestionForm, EditQuestionForm

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
#     context = {
#         'questions': Question.objects.all(),
#         'categories': Category.objects.all(),
#     }
#     return render(request, 'forum/ask.html', context)


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


class QuetsionUpdateView(UpdateView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'forum/update_question.html'
    # fields = ['title', 'question', 'questioner', 'category', 'answered']


class QuestionDeleteView(DeleteView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'forum/delete_question.html'
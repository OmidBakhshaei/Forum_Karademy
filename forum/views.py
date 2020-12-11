# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Question, Category
from .forms import QuestionForm, EditQuestionForm

class HomeListView(ListView):
    model = Question
    template_name = 'forum/home.html'
    # if self.date_updated:
    #     ordering = ['-date_updated']
    # else:
    #     ordering = ['-date_posted']
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


class QuestionsListView(ListView):
    model = Question
    template_name = 'forum/questions.html'
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(QuestionsListView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context
 

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        the_question = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = the_question.get_total_likes()
        liked = False
        if the_question.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(QuestionDetailView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class QuetsionUpdateView(UpdateView):
    model = Question
    form_class = EditQuestionForm
    template_name = 'forum/update_question.html'
    # fields = ['title', 'question', 'questioner', 'category', 'answered']
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(QuetsionUpdateView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'forum/delete_question.html'
    success_url = reverse_lazy('questions')
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(QuestionDeleteView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


class AskQuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'forum/ask.html'
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(AskQuestionCreateView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


class CategoriesListView(ListView):
    model = Question
    template_name = 'forum/categories.html'
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        context = super(CategoriesListView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'forum/category_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        question_menu = Question.objects.all()
        # category_questions = Question.objects.filter()
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context["categories"] = category_menu
        context["questions"] = question_menu
        return context


def like_view(request, pk):
    question = get_object_or_404(Question, id=request.POST.get('question_id'))
    liked = False
    if question.likes.filter(id=request.user.id).exists():
        question.likes.remove(request.user)
        liked = False
    else:
        question.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('question_details', args=[str(pk)]))

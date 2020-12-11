# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
from django.contrib import admin
# from django import forms
from .models import Question, Category, Answer


class QuestionAdmin(admin.ModelAdmin):
    model= Question
    list_display = ('title', 'question', 'topics', 'answered',)
    filter_horizontal = ('category',)
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}

# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Answer)
# admin.site.register(Answer, AnswerAdmin)

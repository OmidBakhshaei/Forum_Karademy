# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'question', 'questioner', 'category',)

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Be specific and imagine you’re asking a question to another person'
            }),
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Include all the information someone would need to answer your question'
            }),
            'questioner' : forms.Select(attrs={'class': 'form-control'}),
            # 'category': forms.CheckboxSelectMultiple(attrs={'class': "form-check form-check-inline"}),
            'category': forms.CheckboxSelectMultiple(),
            # 'answered': forms.CheckboxInput(attrs={'class': "form-check form-check-inline"})
        }


class EditQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'question', 'category', 'answered')

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Be specific and imagine you’re asking a question to another person'
            }),
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Include all the information someone would need to answer your question'
            }),
            # 'category': forms.CheckboxSelectMultiple(attrs={'class': "form-check form-check-inline"}),
            'category': forms.CheckboxSelectMultiple(),
            'answered': forms.CheckboxInput(attrs={'class': "form-check form-check-inline"})
        }
        
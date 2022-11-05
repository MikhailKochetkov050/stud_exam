from django import forms
from django.forms import ModelForm, ModelChoiceField

from TestCreation.models import TeacherTests, Questions


class TeacherTestsForm(ModelForm):

    class Meta:
        model = TeacherTests
        fields = ['test_name', 'attempt_count', 'time']
        labels = {
            'test_name': '',
            'attempt_count': 'Количество попыток прохождения теста',
            'time': 'Время прохождения теста (в минутах)',
        }
        widgets = {
            'test_name': forms.TextInput(attrs={
                'style': "width: 50%", 
                'placeholder': 'Название теста', 
                'id': 'testname', 
                'onkeyup': 'checkParams()', 
                }),
            'attempt_count': forms.NumberInput(attrs={'min': '0', 'id': 'attempt_count', 'onchange': 'checkParams()'}),
            'time': forms.NumberInput(attrs={'min': '0', 'id': 'time', 'onchange': 'checkParams()'}),
        }


class QuestionsForm(ModelForm):

    class Meta:
        model = Questions
        exclude = ['test_id']
        widgets = {
            'question': forms.TextInput(attrs={'style': "width: 80%",}),
            'answer1': forms.TextInput(attrs={'style': "width: 80%",}),
            'answer2': forms.TextInput(attrs={'style': "width: 80%",}),
            'answer3': forms.TextInput(attrs={'style': "width: 80%",}),
            'answer4': forms.TextInput(attrs={'style': "width: 80%",}),
            'prompt': forms.TextInput(attrs={'style': "width: 80%",}),
            'manychoises': forms.CheckboxInput(attrs={'id': 'manychoises', 'name': "manychoises"}),
            'isright1': forms.CheckboxInput(attrs={'id': 'opt1',}),
            'isright2': forms.CheckboxInput(attrs={'id': 'opt2',}),
            'isright3': forms.CheckboxInput(attrs={'id': 'opt3',}),
            'isright4': forms.CheckboxInput(attrs={'id': 'opt4',}),
        }


from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from TestSystem.models import SignUp_Model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Введите логин', widget=forms.TextInput(attrs={
        'type' : "text",
        "name" : "uname",
        'placeholder' : 'Введите логин'
    }))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={
        'type': "password",
        "name": "pwd",
        'placeholder': 'Введите пароль'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя не существует!')
            check_user = SignUp_Model.objects.get(username=username)
            check_user.login_attempts += 1
            if check_user.login_attempts > 5:
                check_user.locked = True
                check_user.save()
            if SignUp_Model.objects.get(username=username).locked:
                raise forms.ValidationError('Пользователь заблокирован! Для разблокирования учетной\
                    записи обратитесь к администратору.')
            if not check_password(password, qs[0].password):
                check_user.save()
                raise forms.ValidationError('Неверный пароль!')
            user = authenticate(username=username, password=password)
            check_user.login_attempts = 0
            check_user.save()
            if not user:
                raise forms.ValidationError('Данный пользователь неактивен!')
        return super().clean(*args, *kwargs)


class SignUpForm(ModelForm):
    user_type = forms.ChoiceField(required=True, label="Тип учетной записи", widget=forms.RadioSelect(
        attrs={'class': 'Radio', 'name': 'user_type', 'onchange': 'checkParams()'}), 
        choices=(('stud','Студент'),('teacher','Преподаватель'),))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'hidden': True, 'id': 'hidden_pwd'}))
    class Meta:
        model = SignUp_Model
        fields = ['full_name', 'user_type', 'username']
        # labels = {'password': (''),}
        widgets = {
            # 'password': forms.PasswordInput(attrs={'hidden': True, 'id': 'hidden_pwd'}),
            'username': forms.TextInput(attrs={'readonly': True, 'id': 'usr'}),
            'full_name': forms.TextInput(attrs={
                'id': 'full_name', 
                'onkeyup': 'checkParams()',
                }),
            }

class ChangeForm(forms.Form):
    # users = forms.ModelMultipleChoiceField(label='Имя пользователя', widget=forms.Select,
    #     queryset=SignUp_Model.objects.all().values_list('username', flat=True)) 
    username =  forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'readonly': True, 'id': 'cngUsrName'}))
    password = forms.CharField(label="Пароль", widget=forms.TextInput(attrs={'readonly': True, 'id': 'cng_pwd'}))
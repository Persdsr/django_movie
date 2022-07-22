from django import forms
from django.contrib.auth.models import User
from django.forms import Textarea

from .models import Movies, Comments
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from captcha.fields import CaptchaField


class AddViewForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=forms.Textarea(attrs={'class': 'text-area form-control', 'rows':3, 'cols':69}))

    field_order = ('name', 'description', 'slogan','age', 'poster', 'year', 'country', 'actors', 'directors', 'budget', 'genres', 'category', 'draft', 'slug')

    class Meta:
        model = Movies
        fields = {'name', 'description', 'slogan','age', 'poster', 'year', 'country', 'actors', 'directors', 'budget', 'genres', 'category', 'draft', 'slug'}


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'text'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'text'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'text'}))
    field_order = ('username', 'email', 'password1', 'password2')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text'}))


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'comment-text', 'placeholder':'Добавить комментарий', 'rows':3, 'cols':69}))

    class Meta:
        model = Comments
        fields = {'text',}




#class ContactForm(forms.ModelForm):
#    """Форма подписки на email"""
#    class Meta:
#        model = Contact
#        fields = '__all__'




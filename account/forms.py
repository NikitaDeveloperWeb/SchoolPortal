from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile,articles


#Форма входа
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Форма регистрации
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


# Редактирование профиля
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name_p','last_name_p','date_of_birth', 'photo')


#для поиска пользователя
class SearchForm(forms.Form):
    keyword = forms.CharField(required=False,max_length=50,label="")

#Написание сообщение
class ArticleForm(ModelForm):
    class Meta:
        model = articles
        fields = ('title','article','photo')
     
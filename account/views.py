from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,UserRegistrationForm, UserEditForm, ProfileEditForm,SearchForm
from django.contrib.auth.decorators import login_required
from .models import Profile,articles
from django.contrib.auth.models import User 
from django.db.models import Q
from django.views import View
from django.db.models import Count
from django.urls import reverse
from django.contrib import auth
from django.core.paginator import Paginator

 

#Функция для аунтификации
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Проверку подлинности успешно')
            else:
                return HttpResponse('Отключенная учетная запись')
        else:
            return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

#Меню чата
@login_required 
def chat(request):
    posts = articles.objects.all().order_by('-published')
    paginator = Paginator(posts,5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)        
    context = {"posts":page.object_list,'page':page,}
    return render(request,'account/news.html',context)    

# Функция для регистрации
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных.
            new_user.save()
            # Создание профиля пользователя.
            Profile.objects.create(user=new_user)
           
            return render(request,
                            'account/register_done.html',
                                    {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

# Редактирование профиля
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                                    data=request.POST,
                                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',
                            {'user_form': user_form,'profile_form': profile_form})
# Функция для поиска
@login_required
def user_search(request): 

    users = Profile.objects.filter()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(first_name_p__icontains=keyword) | Q(last_name_p__icontains=keyword)
        users = Profile.objects.filter(q)
    else:
        keyword = ""
    form = SearchForm(initial={'keyword':keyword})    
    return render(request,'account/search_users.html',{'users':users,'form':form,})





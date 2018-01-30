from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipe.models import Recipe
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

def get_index(request):
    title = "FoodRecipe"
    # 取出資料
    recipes = Recipe.objects.all()
    # locals()可以代替 for recipe in recipe: print(recipe.title)
    return render(request, 'index.html', locals())
    return response

def get_signup(request):
    return render(request, 'signup.html')

 # username/email/password對應form裡面的name=""
def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    
    user = User.objects.create_user(username, email, password)
    if user:
        return redirect('/', locals())
    else:
        redirect('/signup', locals())
    return render(request, 'index.html')

def post_logout(request):
    auth.logout(request)
    return redirect('/')

def post_login(request):
    username = request.POST['username']
    password = request.POST['password']

    #認證到底有無這樣一個會員
    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/', locals())
    else:
        return redirect('/', locals())
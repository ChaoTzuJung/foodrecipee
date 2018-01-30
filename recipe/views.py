from django.shortcuts import render, redirect
#回傳資料改成Json，促使API接口是Json形式
from django.http import JsonResponse
#資料街口
from recipe.models import Recipe
#轉換資料encode
from django.core import serializers
#接收使用者填表單的資料
from django import forms
#內建的訊息框架
from django.contrib import messages
# Create your views here.

#定義類別資料，models要取出哪些欄位使用
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_path', 'description']

def get_recipes_api(request):
    # recipes從model中取出，並可以使用QuerySet API
    recipes =  Recipe.objects.all()
    data = serializers.serialize('json', recipes)
    return JsonResponse({ 'data': data})

def get_create_recipe(request):
    return render(request, 'create_recipe.html')

def get_recipe(request, recipe_id):
    print(recipe_id)
    # 抓出recipe_id，pk就是 primary key，透過pk可以讓Recipe model知道要取出第幾個特定的資料
    recipe = Recipe.objects.get(pk=recipe_id)
    print(recipe)
    return render(request, 'recipe.html', locals())

def post_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            print(new_recipe)
            messages.add_message(request, messages.SUCCESS, '分享成功！')
            return redirect('/', locals())
        else:
            return redirect('/recipes/create')
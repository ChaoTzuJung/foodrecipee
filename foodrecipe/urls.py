from django.contrib import admin
from django.urls import path
#類似path的路由寫法.
from django.conf.urls import url, include

from app.views import get_index, get_signup, post_signup, post_login, post_logout
# 製作API接口
from recipe.views import get_recipes_api, get_create_recipe, post_create_recipe, get_recipe

#代表1個以上的整數，用來取得id，然後\是整數，＋是至少有1個
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', get_signup),
    path('signup/post', post_signup),
    path('login/post', post_login),
    path('logout/post', post_logout),
    path('api/recipes', get_recipes_api),
    url(r'^recipes/(\d+)$', get_recipe),
    path('recipes/create', get_create_recipe),
    path('recipes/create/post', post_create_recipe),
    path('', get_index),
]


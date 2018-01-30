from django.contrib import admin
from recipe.models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')
  
#讓 Recipe 秀在 Admin後台
admin.site.register(Recipe, RecipeAdmin)


from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
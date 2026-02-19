from django.shortcuts import redirect, render
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here
def index(request):
        return render(request, 'index.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {'recipes':recipes}
    return render(request, "recipe_list.html", ctx)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    ctx = {"recipe": recipe}
    return render(request, "recipe_detail.html", ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html' 
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'
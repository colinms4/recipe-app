from django.shortcuts import render
from .models import Recipes
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipesView(LoginRequiredMixin, ListView):    
    model = Recipes
    template_name = 'recipes/main.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipes.objects.all().order_by('name')

class RecipesDetailView(LoginRequiredMixin, DetailView):                       
   model = Recipes                                        
   template_name = 'recipes/detail.html'
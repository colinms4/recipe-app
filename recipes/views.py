from django.shortcuts import render
from .models import Recipes
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm  
import pandas as pd  
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.core.paginator import Paginator
import matplotlib
matplotlib.use('Agg')
from django.db.models import Q, Count
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .utils import get_chart

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

def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None  
    chart = None  
    qs = Recipes.objects.none()  # Initialize an empty queryset
    
    if request.method == 'POST':
        recipe_difficulty = request.POST.get('recipe_difficulty')
        chart_type = request.POST.get('chart_type')
        
        
        qs = Recipes.objects.filter(difficulty=recipe_difficulty)
        if qs:  
            recipes_df = pd.DataFrame(qs.values())
            
            recipes_df['recipe_name'] = recipes_df['name']
            
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
            
            recipes_df = recipes_df.to_html()
    

    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
        'recipes_qs' : qs
    }
    
    return render(request, 'recipes/records.html', context)
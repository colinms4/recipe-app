from django.contrib import admin
from django.urls import path, include
from .views import home, RecipesView, RecipesDetailView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView


app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('list/', RecipesView.as_view(), name='recipes_list'),
    path('list/<pk>/', RecipesDetailView.as_view(), name='recipes_detail'),
    path('records/', views.records, name='records'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('about/', TemplateView.as_view(template_name='recipes/about_me.html'), name='about_me'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
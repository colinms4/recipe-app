from django.contrib import admin
from django.urls import path, include
from .views import home, RecipesView, RecipesDetailView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('list/', RecipesView.as_view(), name='recipes_list'),
    path('list/<pk>/', RecipesDetailView.as_view(), name='recipes_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
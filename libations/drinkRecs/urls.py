from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('find_cocktail', views.find_cocktail),
    path('cocktail/<int:cocktail_id>', views.show_cocktail),
    path('find_similar/<int:cocktail_id>', views.find_similar),
]
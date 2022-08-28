from . import views
from django.urls import path

urlpatterns = [
    path('find/', views.aa_list, name = 'find'),
    # path('find/search/', views.search, name = 'search'),
    path('ali', views.Ali.as_view(), name = 'ali'),
    path('', views.home, name = 'home'),
]
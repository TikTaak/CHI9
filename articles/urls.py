from . import views
from django.urls import path
from .views import ArticleDeleteView  , AticleUpdateView , ArticleCreateView # ,  ArticleDetailView

# app_name = 'articles'

urlpatterns = [
    path('detail/<int:id>', views.articles_detail , name = 'customer_detail'),
    # path('detail/<int:id>', ArticleDetailView.as_view() , name = 'customer_detail_class'),
    path('edit/<int:pk>', AticleUpdateView.as_view(), name = 'customer_edit'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name = 'customer_delete'),
    path('find/search/', views.search, name = 'search'),
    path('new', ArticleCreateView.as_view(), name = 'customer_create'),
    path('', views.articles_list, name = 'customers'),
    #   Tags
    path('tags/', views.tags_list, name = 'tags'),
    path('tags/new/', views.TagCreateView.as_view(), name = 'tags_create'),
    path('tags/delete/<int:pk>', views.TagDeleteView.as_view(), name = 'tags_delete'),
    path('tags/edit/<int:pk>', views.TagUpdateView.as_view(), name = 'tags_edit'),
]
from django.shortcuts import render
from django.views.generic import ListView , DetailView , TemplateView
from django.views.generic.edit import UpdateView , DeleteView  , CreateView
from .models import Article, Tag 
from django.urls import reverse_lazy
from django.db.models import Q
from itertools import chain

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'articles/customers_details.html'

class AticleUpdateView(UpdateView):
    model = Article
    fields = ('name', 'describtion', 'National_code', )
    template_name = 'articles/customers_edit.html'
    success_url = reverse_lazy('customers')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/customers_delete.html"
    success_url = reverse_lazy('customers')

class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/customers_create.html"
    fields = ('name','tags', 'National_code', 'auther', 'describtion') #, 
    success_url = reverse_lazy('customers')




def articles_list(request):
    articles_list = Article.objects.all()
    context = {
        "articles_list": articles_list 
    }
    return render(request, "articles/customers.html", context)


def articles_detail(request, id):
    articles_id = Article.objects.get(id=id)
    tags = Tag.objects.all().filter(articles = articles_id)
    context = {
        "tags": tags ,
        "articles_id": articles_id , 
    }
    return render(request, "articles/customers_details.html", context)

def search(request): #by id
    if (request.method == "GET"):
        q = request.GET.get("search")

    articles_list = Article.objects.filter(Q(name__contains=q) | Q(pk__contains=q) | Q(describtion__contains=q))
    # articles_list = Article.objects.filter(name__icontains = q)
    return render(request, "articles/customers_find.html", {"articles_list":articles_list})



#   Tags

class TagUpdateView(UpdateView):
    model = Tag
    fields = ('title', 'slug')
    template_name = 'tags/tags_edit.html'
    success_url = reverse_lazy('tags')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/tags_delete.html"
    success_url = reverse_lazy('tags')

class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/tags_create.html"
    fields = ('title', 'slug') 
    success_url = reverse_lazy('tags')


def tags_list(request):
    tags_list = Tag.objects.all()
    context = {
        "tags_list": tags_list 
    }
    return render(request, "tags/tags_list.html", context)

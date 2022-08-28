from re import T
from django.shortcuts import render
from .models import Aa
from django.views.generic import TemplateView

def home(request):
    context = {}
    return render(request, "pages/home.html", context)

def aa_list(request):
    aa_list = Aa.objects.all()
    context = {
        "aa_list": aa_list
    }
    return render(request, "pages/find.html", context)

# def search(request): #by id
#     if (request.method == "GET"):
#         q = request.GET.get("search")

#     aa_list = Aa.objects.filter(pk__icontains = q)
#     return render(request, "pages/find.html", {"aa_list":aa_list})

class Ali(TemplateView):
    template_name = "pages/ali.html"


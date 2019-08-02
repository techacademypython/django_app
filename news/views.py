from django.shortcuts import render
from .models import News


# Create your views here.

def home_view(request):
    context = {}
    context["news_list"] = News.objects.filter(title__icontains="asdas")
    return render(request, "index.html", context)

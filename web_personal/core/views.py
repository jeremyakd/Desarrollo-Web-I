from django.shortcuts import render

# crear 4 funciones home about portfolio y contact.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

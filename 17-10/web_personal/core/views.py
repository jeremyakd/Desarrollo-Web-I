from django.shortcuts import render, HttpResponse

# Create your views here.
html_response = "<h1> web personal<h1/>"

def home(request):
    return HttpResponse(html_response + "<h2> Portada <h2/>")


def about(request):
    return HttpResponse(html_response + "<h2> Acerca de <h2/> <p> Me llamo jeremias y soy programador.</p>")


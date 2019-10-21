from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """

<h1> web personal<h1/>
<ul>
    <li><a href="/home/"> PORTADA </a></li>
    <li><a href="/about/"> ACERCA DE </a></li>
    <li><a href="/portfolio/"> PORTAFOLIO </a></li>
    <li><a href="/contact/"> CONTACTO </a></li>
</ul>

"""

def home(request):
    return HttpResponse(html_base + "<h2> Portada <h2/>")


def about(request):
    return HttpResponse(html_base + "<h2> Acerca de <h2/> <p> Me llamo jeremias y soy programador.</p>")

# crear funcino contact y portfolio 

def portfolio(request):
    return HttpResponse(html_base + """
    <h2> Portafolio </h2>
    <p> estos son mis laburos .... </p>
    """
    )

def contact(request):
    return HttpResponse(html_base + """
    <h2> Contacto </h2>
    <p> mandame un mail 
    
    """)
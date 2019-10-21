from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

# refactorizar funcion about, contact y portfolio 

# html_base da ERROR porque no existe la  virable !!!!!!!

def about(request):
    return HttpResponse(html_base + 
    """
    <h2> Acerca de </h2>
    <p> Me llamo jeremias y soy programador.</p>
    """)



def portfolio(request):
    return HttpResponse(html_base + """
    <h2> Portafolio </h2>
    <p> estos son mis laburos .... </p>
    """
    )

def contact(request):
    return HttpResponse(html_base + """
    <h2> Contacto </h2>
    <p> mandame un mail <a href="mailto:jeremyakd@gmail.com"> acá</a></p>
    
    """)
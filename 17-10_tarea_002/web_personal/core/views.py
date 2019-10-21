from django.shortcuts import render, HttpResponse

# Create your views here.

html_response = '''
<ul>
   <li><a href='/'>Portada</a></li>
   <li><a href='/about'>Acerca de</a></li>
   <li><a href='/portfolio'>Portafolio</a></li>
   <li><a href='/contact'>Contacto</a></li>
</ul> '''

def home(request):
    return HttpResponse(html_response + "<h1> Portada </h1>")

def about(request):
    return HttpResponse(html_response + "<h1> Acerca de </h1> <h2> Biografía </h2> <p> Me llamo <b>Django</b>. The D is silent. </p>")

def portfolio(request):
    return HttpResponse(html_response + "<h1> Portafolio </h1> <h2> Currículum </h2> <b>Segundo proyecto</b> ... <u>Más información</u> <p> <b>Primer proyecto</b> ... <u>Más información</u>")

def contact(request):
    return HttpResponse(html_response + "<h1> Contacto </h1> <h2> Asesoría </h2> <b>Teléfono:</b> número (+54 11) <p> <b>Honorarios:</b> precio (U$S)")
   

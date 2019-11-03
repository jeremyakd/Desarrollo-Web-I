from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = '<h1>Web Personal</h1>'

def home(request):
    return HttpResponse(html_base + '<h2><mark>Portada</mark></h2>')

def about(request):
    return HttpResponse(html_base + 
    '''
    <h2>Acerca de</h2>
    <h3>Biografía</h3>
    
    <p>Me llamo Django. The D is silent.</p>
    ''')

def portfolio(request):
    return HttpResponse(html_base + 
    '''
    <h2>Portafolio</h2>
    <h3>Currículum</h3>
    
    <p>Enlace a proyectos...</p>
    ''')

def contact(request):
    return HttpResponse(html_base + 
    '''
    <h2>Contacto</h2>
    <h3>Asesoría</h3>
    
    <p>Email: (@)</p>
    <p>Teléfono: (+54 11)</p>
    <p>Honorarios: (U$S)</p>
    ''')

from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    
    return render(
        request,
        'index.html', 
        {
            'public_flans': public_flans
        }
)

def acerca(request):
    return render(request, 'about.html', {})

def ubicacion(request):
    return render(request, 'ubicacion.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)    
    
    return render(
        request,
        'welcome.html', 
        {
            'private_flans': private_flans
        }
    ) 
    #return render(request, 'welcome.html', {})

def contacto(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactFormModelForm(request.POST)
        #form = ContactFormForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito/')
        
    else:
        form = ContactFormForm()          
          
    return render(request, 'contact.html', {'form': form})

def exito(request):
    
    return render(request, 'success.html', {})

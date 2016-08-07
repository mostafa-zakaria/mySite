from django.shortcuts import render
from .models import Disease
#from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse('<h1>Greetings Mortal Fool!!</h1>')
	context = {
	"diseases": Disease.objects.all()
	}
	return render(request, 'index.html', context) #used to render index.html in templates directory



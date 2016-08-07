from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse('<h1>Greetings Mortal Fool!!</h1>')
	context = {
	"diseases": diseases
	}
	return render(request, 'index.html', context) #used to render index.html in templates directory

class Disease:
	def __init__(self, name, pain, survivability):
		self.name = name
		self.pain = pain
		self.survivability = survivability

diseases = [ 
	Disease("Zika Virus", "Very High", 90),
	Disease("Ebola", "Bleeding from the Eyes Extreme", 0),
	Disease("Gonorrhea", "Mild", 50)
]
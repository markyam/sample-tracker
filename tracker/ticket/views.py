from django.http import HttpResponse

def home(request, name=None):
	if name:
		return HttpResponse("Hello %s !" % name)
	else:
		return HttpResponse("Hello World !")

	

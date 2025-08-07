from django.http import HttpResponse

def home(request):
  return HttpResponse("Hello from Aqib.")

def about(request):
  return HttpResponse("Welcome to about page.")

def contact(request):
  return HttpResponse("This is out contact page.")
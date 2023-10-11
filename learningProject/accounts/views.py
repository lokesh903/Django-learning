from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

peoples = [
    {"name":'abhijeet Gupta','age': 26},
    {"name":'Ravi','age': 36},
    {"name":'Raviish','age': 46},
]

def home(request):
    return HttpResponse("hey i am lucky.")
def successPage(request):
    return render(request,'home/index.html',context={'peoples':peoples})
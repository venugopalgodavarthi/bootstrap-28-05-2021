from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,"sample.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def gallary(request):
    return render(request,"gallary.html")

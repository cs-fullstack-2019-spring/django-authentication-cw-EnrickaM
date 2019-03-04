from django.shortcuts import render
from django .http import HttpResponse
from .forms import foodfitnessForm
from django.contrib.auth.models import User
# Create your views here.
# code below alllows your function to bring up you home page while i likned it to my form.
def index(request):
    return render(request,'foodfitnessApp/index.html')

#code below brings up the form with different infromation i want from you.
def newuser(request):
    form=foodfitnessForm(request.POST or None)
    context={
            "form":form
        }

    return render(request, 'foodfitnessApp/newuser.html',context)

#code below redirects you to a page that says' welocme user '
def createnewuser(request):
    if request.method == "POST":
        user =User.objects.create_user(request.POST['username'])
        return render(request,'foodfitnessApp/createnewuser.html')
    else:
        return HttpResponse("Error")
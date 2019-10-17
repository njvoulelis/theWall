from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User


def loginReg(request):
    return render(request, "logRegApp/loginReg.html")

def process(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hashedPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        newUser = User.objects.create(firstName=request.POST["firstName"], lastName=request.POST["lastName"], username=request.POST["username"], email=request.POST["email"], password=hashedPass)
        newUser.save()
        request.session['userid'] = newUser.id
        request.session['username']=newUser.username
        return redirect("/success")

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        loggedUser = user[0] #retrieves first object in list filtered by email two lines above
        print (loggedUser.username) 
        if bcrypt.checkpw(request.POST['password'].encode(), loggedUser.password.encode()):
            request.session['userid'] = loggedUser.id
            request.session['username'] = loggedUser.username
            return redirect('/wall')
    messages.error(request, "Login error: User doesn't exist")
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def success(request):
    if 'username' in request.session:
        return render(request, "logRegApp/success.html")
    else:
        messages.error(request, "Please log in to view that page")
        return redirect("/")
    
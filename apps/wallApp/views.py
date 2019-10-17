from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Comment
from apps.logRegApp.models import User

def viewWall(request):
    if 'username' in request.session:
        context = {
            'messages': Message.objects.all(),
        }
        return render(request, "wallApp/viewWall.html", context)
    else:
        messages.error(request, "Please log in to view the wall")
        return redirect("/")


def postMessage(request):
    newMessage = Message.objects.create(user=User.objects.get(id = request.session['userid']), message = request.POST['postMessage'])
    print("#"*80)
    print(request.POST['postMessage'])
    print(newMessage.id)
    print(request.POST['messageID'])
    newMessage.save()
    return redirect("/wall")

def postComment(request):
    print("%"*80)
    print(request.POST['messageID'])
    newComment = Comment.objects.create(user=User.objects.get(id = request.session['userid']), message = Message.objects.get(id=request.POST['messageID']), comment = request.POST['postComment'])
    print("$"*80)
    newComment.save()
    return redirect("/wall")

def deleteComment(request):
    print("trying to delete")
    commentToDelete = Comment.objects.get(id= request.POST['commentID'])
    commentToDelete.delete()
    return redirect("/wall")


from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def home(request):
    board = Board.objects
    return render(request, "home.html", {"board" : board})

def submit(request):
    b = Board()
    b.content = request.GET['content']
    b.writer = request.GET['writer']
    b.day = request.GET['day']
    b.save()
    return redirect('/')

def contributor(request):
    board = Board.objects
    return render(request, "contributor.html", {"board" : board})

def new(request):
    return render(request, "new.html")
    
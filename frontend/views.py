from django.shortcuts import render

# Create your views here.

def todoList(request):
    return render(request, 'frontend/list.html')
from django.shortcuts import render, HttpResponse

def login(request):
    """
        Homepage
        Página home
    """
    return HttpResponse("Hello, World. You're at the Login page.")

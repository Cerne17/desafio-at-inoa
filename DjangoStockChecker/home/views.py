from django.shortcuts import render, HttpResponse

def index(request):
    """
        Homepage
        Página home
    """
    # return render(request, "home/index.html", {})
    return HttpResponse("Hello, World. You're at the home page.")

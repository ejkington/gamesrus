from django.shortcuts import render


def index(request):
    """ View for returning index page """

    return render(request, 'home/index.html')
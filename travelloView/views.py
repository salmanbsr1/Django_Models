from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from . models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Canada"
    dest1.desc = "This is Canada Deescription "
    dest1.image = "static/images/destination_1.jpg"
    dest1.price = 900

    dest2 = Destination()
    dest2.name = "Destination 2"
    dest2.desc = "This is Canada Deescription "
    dest2.image = "static/images/destination_2.jpg"
    dest2.price = 800

    dest3 = Destination()
    dest3.name = "Destination 3"
    dest3.desc = "This is Canada Deescription "
    dest3.image = "static/images/destination_3.jpg"
    dest3.price = 600

    dests = [dest1,dest2,dest3]

    return render(request, "index.html", {'dests': dests})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def destinations(request):
    return render(request, "destinations.html")


def news(request):
    return render(request, "news.html")


def elements(request):
    return render(request, "elements.html")

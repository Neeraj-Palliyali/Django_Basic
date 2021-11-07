from django.http import response
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
import challenges

monthly_challenges = {
    "january": "Eat no meat for a month",
    "february": "Walk for an hour daily",
    "march": "Learn Django for 3 hrs",
    "april": "Learn Django for 3 hrs",
    "may": "Walk for an hour daily",
    "june": "Eat no meat for a month",
    "july": "Learn Django for 3 hrs",
    "august": "Walk for an hour daily",
    "september": "Eat no meat for a month",
    "october": "Learn Django for 3 hrs",
    "november": "Walk for an hour daily",
    "december": "Eat no meat for a month",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if(month > len(months)):
        return HttpResponseNotFound("Invalid Month")
    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if(month in monthly_challenges.keys()):
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")


def index(request):

    months = list(monthly_challenges.keys())

    list_items = ""

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li> <a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul> {list_items} </ul"
    return HttpResponse(response_data)

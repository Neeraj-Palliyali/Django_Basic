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
        return HttpResponse(monthly_challenges[month])
    else:
        return HttpResponseNotFound("This month is not supported")

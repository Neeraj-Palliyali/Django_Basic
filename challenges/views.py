from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month):
    if( month == 'january'):
        challenge_text = "Eat no meat for a month"
    
    elif(month == "february"):
        challenge_text = "Walk for an hour daily"
    
    elif(month == "march"):
        challenge_text = "Learn Django for 3 hrs"

    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)    
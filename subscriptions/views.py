from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Subscription

def subscription_signup(request):
    if request.method == "POST":
        subscription = Subscription(
            email=request.POST["email-input"],
            unsubscribed=False
        )
        subscription.save()
        template = loader.get_template('subscriptions/signup_success.html')
        return HttpResponse(template.render(None, request))
    template = loader.get_template('subscriptions/signup.html')
    return HttpResponse(template.render(None, request))
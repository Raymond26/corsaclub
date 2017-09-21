from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Subscription

def subscription_signup(request):
    if request.method == "POST":
        email_input = request.POST["email-input"]
        check_existing = Subscription.objects.filter(email=email_input)
        template = loader.get_template('subscriptions/signup_success.html')
        if len(check_existing) > 0:
            return HttpResponse(template.render(None, request))
        subscription = Subscription(
            email=request.POST["email-input"],
            unsubscribed=False
        )
        subscription.save()
        return HttpResponse(template.render(None, request))
    template = loader.get_template('subscriptions/signup.html')
    return HttpResponse(template.render(None, request))
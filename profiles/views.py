from django.shortcuts import render
from .models import UserProfile, Session, PageView
from django.utils.timezone import now
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import datetime

def check_generated_id(generated_id, generate_function):
    check = UserProfile.objects.filter(id=generated_id)
    if len(check) == 1:
        regenerate_id = generate_function()
        return check_generated_id(regenerate_id, lambda: generate_function)
    else:
        return generated_id


@csrf_exempt
def sync_customer_product_user(request):
    if request.method != "POST":
        return HttpResponseBadRequest("wrong method")
    json_req = json.loads(request.body)
    now_ts = now()
    our_id = None
    user_obj = None
    if "user_profile_id" not in json_req:
        print("new user")
        id_gen_function = lambda: random.getrandbits(32)
        new_user = UserProfile(
            id=check_generated_id(id_gen_function(), id_gen_function),
            last_seen_timestamp=now_ts,
            first_seen_timestamp=now_ts,
            session_count=1
        )
        new_user.save()
        our_id = new_user.id
        user_obj = new_user
    else:
        our_id = int(json_req["user_profile_id"])
        users = UserProfile.objects.filter(id=our_id)
        if len(users) == 0:
            return HttpResponseNotFound("user not found with that id")
        else:
            user = users[0]
            user.last_seen_timestamp=now_ts
            user.session_count += 1
            user.save()
            user_obj = user

    latest_session = Session.objects.filter(user_profile=user_obj).filter(latest_request_timestamp__gte=now() - datetime.timedelta(minutes=30))
    if len(latest_session) == 0:
        latest_session = Session(
            user_profile=user_obj,
            platform=Session.SessionPlatform.WEB.value
        )
        latest_session.save()
    else:
        latest_session = latest_session[0]
        latest_session.latest_request_timestamp = now()
        latest_session.save()

    page_view = PageView(
        user_profile = user_obj,
        session=latest_session,
        path = json_req["location"],
        timestamp = now()
    )
    page_view.save()
    response_data = {
        "id" : our_id
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
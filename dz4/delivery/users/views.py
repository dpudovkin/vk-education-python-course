import json

from django.http import JsonResponse, Http404
from django.shortcuts import render


def user_list(request):
    if request.method == "GET":
        userList = {
            {"Name": "Alex", "Age": "18", "Date of birth": "04.11.2001"},
            {"Name": "Dima", "Age": "19", "Date of birth": "04.11.2001"},
            {"Name": "Sergey", "Age": "20", "Date of birth": "04.11.2001"}
        }
        return JsonResponse(json.dumps(userList))
    else:
        raise Http404  # TODO change exception


def user_info(request):
    if request.method == "GET":
        userInfo = {"Name": "Alex", "Age": "18", "Date of birth": "04.11.2001"}
        return JsonResponse(json.dumps(userInfo))
    else:
        raise Http404  # TODO change exception


def create_user(request):
    if request.method == "POST":
        # TODO create user
        userInfo = {"CreatedUserID": "Alex"}
        return JsonResponse(json.dumps(userInfo))
    else:
        raise Http404  # TODO change exception

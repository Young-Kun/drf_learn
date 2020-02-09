from django.shortcuts import render, HttpResponse
import json

user_dict = {
    'username': 'zhu',
    'sex': 'male',
    'age': 18
}


def userList(request):
    return HttpResponse(json.dumps(user_dict), content_type='application/json')

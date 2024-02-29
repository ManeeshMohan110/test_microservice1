from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)

from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import AccountBase
from django.contrib.auth import authenticate, login, logout


def get_user(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user)
        user_response = get_object_or_404(AccountBase, email=email )
        return JsonResponse({"user_is_authenticated":True, "username":user_response.username}, safe=False)
    
    return JsonResponse({"user_is_authenticated":False, "username":"Annonymous"}, safe=False)

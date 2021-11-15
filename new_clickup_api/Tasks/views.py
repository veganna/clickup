import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from Accounts.models import AccountBase
from django.shortcuts import get_object_or_404
# Create your views here.




def get_task(request):
    if request.GET.get("data_User"):
        user = get_object_or_404(AccountBase, username=request.GET.get("data_User")) 
        if user is not None:
            getTask = Task.objects.filter(assign_to = user)
        else:
            return JsonResponse({"error":"User Is Not Recognized"}, safe=False)
    else:
        return JsonResponse({"error":"User Is Not Recognized"}, safe=False)

    getTaskJson = []
    for i in getTask:
        if i not in getTaskJson:
            getTaskJson.append(i)
    
    return JsonResponse(json.dumps(getTaskJson), safe=False)

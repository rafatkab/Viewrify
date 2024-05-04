from django.shortcuts import render
from django.http import JsonResponse

def my_json_view(request):
    return JsonResponse("Hello World", safe=False)
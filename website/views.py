from django.shortcuts import render
from wiki import all_text
import json
from django.http import HttpResponse

def home(request):
    return render(request, 'index') #Index is a file in /templates


def homeInputJson(request):
    query = request.GET['query']
    result = all_text(query)
    jsonData = json.dumps(result)
    print jsonData
    return HttpResponse(jsonData, content_type="application/json")


def homeInput(request):
    return render(request, 'query', {})
    

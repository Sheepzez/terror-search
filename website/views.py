from django.shortcuts import render

def home(request):
    return render(request, 'index') #Index is a file in /templates


def homeInput(request):
    query = request.GET['query']
    
    return render(request, 'query', {'query':query})
    

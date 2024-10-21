from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LongToShort

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def home(request):
    context = {"submitted": False, 'error': False}
    
    if request.method == "POST":
        data = request.POST 
        long_url = data['longurl']
        custom_name = data['custom_name']
        
                
        try:
            obj = LongToShort(long_url = long_url, short_url = custom_name)
            obj.save()
        
            date = obj.date
            clicks = obj.clicks
            
            
            context['clicks'] = clicks
            context['date'] = date
            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context['submitted'] = True 
        except:
            context['error'] = True
    else:
        print("User is not sending anything")
        
    
    return render(request, "index.html", context) 


def task(request):
    context = {
        "name": "Mahesh",
        "x" : 10,
    }
    return render(request, "test.html", context)


def redirect_url(request, shorturl):
    row = LongToShort.objects.filter(short_url = shorturl)
    
    if len(row) == 0:
        return HttpResponse("No such url exists")
    
    obj = row[0]
    long_url = obj.long_url
    obj.clicks += 1
    obj.save()
    
    return redirect(long_url)
    
    
def analytics(request):
    rows = LongToShort.objects.all()
    context = {"row":rows}
    return render(request, "all-analytics.html", context)
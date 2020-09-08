from django.shortcuts import render
from datetime import date, datetime

# Create your views here.
def index(request):
    return render(request, "weekend/index.html",{
        "weekend": date.today().weekday == 5 or date.today().weekday == 6
    })


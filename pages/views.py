from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, state_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    realtors_mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtor,
        'mvp_realtors': realtors_mvp,
    }
    return render(request, 'pages/about.html', context)


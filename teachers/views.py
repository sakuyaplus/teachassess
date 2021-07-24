from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from .models import Teacher
# Create your views here.
def index(request):
    listings = Teacher.objects.all().filter(show=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={
        'listings': paged_listings
    }
    return render(request, 'teachers/teachers.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Teacher, pk=listing_id)
    context = {
        'listing': listing
    }


    return render(request, 'teachers/listing.html', context)

def search(request):

    context= {
        
    }
    return render(request, 'teachers/search.html', context)
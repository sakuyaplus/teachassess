from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


# Create your views here.
def index(request):

    context={
      
  
    }
    return render(request, 'teachers/teachers.html',context)

def listing(request, listing_id):
   
    context = {
        
    }


    return render(request, 'teachers/listing.html', context)

def search(request):

    context= {
        
    }
    return render(request, 'teachers/search.html', context)
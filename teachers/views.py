from tcomments.models import TComment
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from academies.models import Academy
from .models import Teacher
# Create your views here.
def index(request):
    listings = Teacher.objects.all().filter(show=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    academies=Academy.objects.all()
    context={
        'listings': paged_listings,
        'academies': academies,
    }

    return render(request, 'teachers/teachers.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Teacher, pk=listing_id)
    comments = TComment.objects.order_by('-comment_date').filter(
        teacher_id=listing_id
    )
    commentcounts = len(comments)
    context = {
        'listing': listing,
        'comments': comments,
        'commentcounts': commentcounts,
    }


    return render(request, 'teachers/listing.html', context)

def search(request):

    context= {
        
    }
    return render(request, 'teachers/search.html', context)
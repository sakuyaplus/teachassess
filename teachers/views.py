from tcomments.models import TComment
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.db.models import Q,Avg
from .models import Teacher
from .choices import academy_choices,rank_choices
# Create your views here.
def index(request):
    listings = Teacher.objects.all().filter(show=True)


    if 'q' in request.GET:
        keywords=request.GET['q']
     
        if keywords:
            listings = listings.filter(
                Q(name__icontains=keywords)|Q(contact__icontains=keywords)|Q(studyexp__icontains=keywords)
                |Q(researchfield__icontains=keywords)
            )

    if 'academy' in request.GET:
        academy=request.GET['academy']
      
        if academy !='全部':
            listings = listings.filter(
                dept__iexact=academy
            )

    if 'rank' in request.GET:
        rank=request.GET['rank']

        if rank !='全部':
            listings = listings.filter(
                rank__icontains=rank
            )   

    if 'sort' in request.GET:
        sort=request.GET['sort']

        if sort == '1':
            listings = listings.order_by('englishname')
        if sort == '2':
            listings = listings.order_by('-englishname')

    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
        
    context={
        'listings': paged_listings,
        'academy_choices':  academy_choices,
        'rank_choices': rank_choices,
        'values': request.GET
    }
   
    return render(request, 'teachers/teachers.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Teacher, pk=listing_id)
    comments = TComment.objects.order_by('-comment_date').filter(
        teacher_id=listing_id
    )
    avgscore=TComment.objects.filter(teacher_id=listing_id).aggregate(Avg("stars"))['stars__avg']
    if avgscore==None:
        avgscore=0
    commentcounts = len(comments)
    context = {
        'listing': listing,
        'comments': comments,
        'commentcounts': commentcounts,
        'avgscore': avgscore,
    }


    return render(request, 'teachers/listing.html', context)

def search(request):

    context= {
        
    }
    return render(request, 'teachers/search.html', context)


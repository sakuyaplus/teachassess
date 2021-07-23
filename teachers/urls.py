from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='teachers'),
    path('<int:listing_id>', views.listing, name='teacherlisting'),
    path('search', views.search, name='teachersearch')
]
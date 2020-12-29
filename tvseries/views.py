from django.shortcuts import render

# Create your views here.
from tvseries.models import SearchTerm


def home_view(request):
    return render(request, 'home.html', {})


def search_view(request):
    search_terms = SearchTerm.objects.all().values_list('search_term', flat=True)[:5]
    popular_searches = SearchTerm.objects.all().order_by('-count').values_list('search_term', flat=True)[:5]
    return render(request, 'utils/tv-series-finder.html', {'search_terms': search_terms, 'popular_searches': popular_searches})

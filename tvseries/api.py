from datetime import datetime

import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response
from rest_framework.views import APIView

from tvseries.models import SearchTerm, TvSeries
from tvseries.serializer import TvSeriesSerializer


class TvSeriesSearchView(APIView):
    @staticmethod
    def get(request):
        url = "http://api.tvmaze.com/search/shows"
        search_query = request.GET.get("search_query")
        length = request.GET.get("length")

        search_term, created = SearchTerm.objects.get_or_create(search_term=search_query)
        hard_refresh = request.GET.get("hard_refresh")

        time_difference = 0
        if not created and search_term.search_date:
            time_difference = int((datetime.now().date() - search_term.search_date).days)

        if created or hard_refresh or time_difference > 10:
            print('New Data Updated')
            params = {'q': search_query}
            r = requests.get(url=url, params=params)

            data = r.json()

            if len(data) == 0:
                return Response('No Data Found')

            for x in data:
                tv_series, tv_series_created = TvSeries.objects.get_or_create(name=x['show']['name'])

                if tv_series_created or hard_refresh or time_difference > 10:
                    show = x['show']
                    tv_series.name = show.get('name')
                    tv_series.url = show.get('url')
                    tv_series.language = show.get('language')
                    tv_series.rating = show.get('rating').get('average')
                    tv_series.image = None if show.get('image') is None else show.get('image').get('medium')
                    tv_series.summary = show.get('summary')

                tv_series.search_term.add(search_term)
                tv_series.save()

            search_term.search_date = datetime.now()

        search_term.count = search_term.count + 1
        search_term.save()

        results = search_term.tvseries_set.all()
        total = len(results)
        paginator = Paginator(results, length)
        page = request.GET.get('page')

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page = 1
            results = paginator.page(page)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page = paginator.num_pages
            results = paginator.page(page)

        serialized = TvSeriesSerializer(results, many=True)
        return Response({'total': total, 'length': length, 'current': page, 'data': serialized.data})

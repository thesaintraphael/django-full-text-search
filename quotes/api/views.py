from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity

from rest_framework.generics import ListAPIView


from .serializers import QuoteSerializer
from ..models import Quote


class QuoteListAPIView(ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    @property
    def search_term(self):
        return self.request.query_params.get("search", "")

    def _apply_basic_search(self, qs):
        """Searching whether the name or quote contains search term

        Note: after adding django.contrib.postgres.search to installed apps, Single field searches (with Q object or simple filter)
              will be treated as full-text searches.

        """

        return qs.filter(
            Q(name__icontains=self.search_term) |
            Q(quote__icontains=self.search_term)
        )

    def _annotate_with_search_vector(self, qs):
        """Annotating the queryset with search vector"""

        return qs.annotate(search=SearchVector("name", "quote"))

    def get_queryset(self):

        if self.search_term:

            # fields that will be searched
            search_vector = SearchVector(
                "name", weight="B") + SearchVector("quote", weight="A")

            # translates the words provided to us as a query from the form, passes them through a
            # stemming algorithm, and then it looks for matches for all of the resulting terms.
            search_query = SearchQuery(self.search_term)

            # allow us to order the results by the relevance of the search
            rank = SearchRank(search_vector, search_query)

            # apply the search
            return super().get_queryset().annotate(search=search_vector, rank=rank
                                                   ).filter(search=search_query, rank__gt=0.001).order_by("-rank")

        return super().get_queryset()


class QuoteListAPIViewWithSimilarity(QuoteListAPIView):

    def get_queryset(self):
        if self.search_term:

            print("?")

            return Quote.objects.all().annotate(similarity=TrigramSimilarity("quote", self.search_term)
                                                ).filter(similarity__gt=0.01).order_by("-similarity")

        return super().get_queryset()

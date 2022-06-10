from django.db.models import Q
from django.contrib.postgres.search import SearchVector

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
        """Annotaing the queryset with search vector"""

        return self._annotate_with_search_vector(self.queryset).filter(search=self.search_term)

from rest_framework.generics import ListAPIView
from django.db.models import Q


from .serializers import QuoteSerializer
from ..models import Quote


class QuoteListAPIView(ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def _apply_basic_search(self, qs):
        """Searching whether the name or quote contains search term"""

        search = self.request.query_params.get("search", "")

        return qs.filter(
            Q(name__icontains=search) |
            Q(quote__icontains=search)
        )

    def get_queryset(self):
        return self._apply_basic_search(super().get_queryset())

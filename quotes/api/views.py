from rest_framework.generics import ListAPIView


from .serializers import QuoteSerializer
from ..models import Quote


class QuoteListAPIView(ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

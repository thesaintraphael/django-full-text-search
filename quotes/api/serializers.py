from rest_framework import serializers

from ..models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        exclude = ("created_at", "updated_at")

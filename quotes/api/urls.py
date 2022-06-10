from django.urls import path

from . import views

app_name = 'quotes-api'

urlpatterns = [
    path("list/", views.QuoteListAPIView.as_view(), name="list"),
]

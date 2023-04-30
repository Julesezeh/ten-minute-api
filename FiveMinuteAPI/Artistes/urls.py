from django.urls import path
from .views import ListArtistesView, DetailArtistesView

urlpatterns = [
    path("",ListArtistesView.as_view()),
    path("<int:pk>",DetailArtistesView.as_view())
]
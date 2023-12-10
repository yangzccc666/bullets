from django.urls import path
from bullets_game.views import index

urlpatterns = [
    path("", index, name="index"),
]

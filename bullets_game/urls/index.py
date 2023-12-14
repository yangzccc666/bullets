from django.urls import path, include
from bullets_game.views.index import index


urlpatterns = [
    path("", index, name="index"),
    path("menu/", include("bullets_game.urls.menu.index")),
    path("playground/", include("bullets_game.urls.playground.index")),
    path("settings/", include("bullets_game.urls.settings.index")),
]


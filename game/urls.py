from django.urls import path
from . import views

from .views import(
       HomeView,
       RegisterView,
       LoginView,
       play_game,
       reset_game,
       logout_view,
       jugar,
       LanguageView,
       reset_juego,
       leaderboard_view,
       
)

app_name= 'game'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),   
    path('singup/', RegisterView.as_view(), name='singup'),   
    path('login/', LoginView.as_view(), name='login'),
    path('language/', LanguageView.as_view(), name='language'),   
    path("play/", views.play_game, name="play"),
    path("jugar/", views.jugar, name="jugar"),
    path("reset/", views.reset_game, name="reset"),
    path("reiniciar/", views.reset_juego, name="reiniciar"),
    path("logout/", views.logout_view, name="logout"),
    path("leaderboard/", views.leaderboard_view, name="leaderboard"),

]

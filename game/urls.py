from django.urls import path
from . import views

from .views import(
       HomeView,
       RegisterView,
       LoginView,
       play_game,
       reset_game,
)

app_name= 'game'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),   
    path('singup/', RegisterView.as_view(), name='singup'),   
    path('login/', LoginView.as_view(), name='login'),  
    path("play/", views.play_game, name="play"),
    path("reset/", views.reset_game, name="reset"),

]

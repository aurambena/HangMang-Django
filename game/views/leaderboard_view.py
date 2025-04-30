from game.models import PlayerStats
from django.shortcuts import render

def leaderboard_view(request):
    stats = PlayerStats.objects.all().order_by('-victories', 'games_played')
    return render(request, "game/leaderboard.html", {"stats": stats})

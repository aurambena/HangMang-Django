from game.models import PlayerStats, EstadisticasJugador
from django.shortcuts import render

def leaderboard_view(request):
    stats = PlayerStats.objects.all().order_by('-victories', 'games_played')
    estadisticas = EstadisticasJugador.objects.all().order_by('-victorias', 'juegos_jugados')
    context = {
        'stats': stats,
        'estadisticas': estadisticas

    }
    return render(request, "game/leaderboard.html", context)




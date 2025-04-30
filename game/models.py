from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
       
class PlayerStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    victories = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Player Stat'
        verbose_name_plural = 'Player Stats'

    def __str__(self):
        return f"{self.user.username} - Wins: {self.victories}, Games: {self.games_played}"
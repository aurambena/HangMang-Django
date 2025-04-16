from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField('Birth date', null=True, blank=True)

    # Sets how names will appear in the admin
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username
    
class UserGame(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_game', verbose_name='user')
    nickname = models.CharField(max_length=10, blank=True)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        blank=True,
        null=True
    )
    
    # Sets how names will appear in the admin
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user.username
    

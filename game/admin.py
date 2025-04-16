from django.contrib import admin
from .models import UserGame

# Register your models here.
@admin.register(UserGame)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserGame
    list_display = ('user', 'nickname', 'age','pk')
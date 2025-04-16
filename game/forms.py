from django import forms
from .models import UserGame, UserProfile
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'

        ]

    def save(self):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()

        from .models import UserProfile
        UserProfile.objects.create(user=user)

        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=140, label='username')
    password = forms.CharField( label='password', widget=forms.PasswordInput())


class LetterForm(forms.Form):
    letter = forms.CharField(
        max_length=1,
        label='Guess a letter',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A-Z'})
    )
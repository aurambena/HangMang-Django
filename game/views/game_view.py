
from game.models import UserGame
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from game.forms import AccountForm, LoginForm
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class LanguageView(TemplateView):
    template_name = "language.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class RegisterView(CreateView):
      model = User
      template_name = 'register.html'
      success_url = reverse_lazy('game:login')
      form_class= AccountForm

      def form_valid(self, form):
          messages.add_message(self.request, messages.SUCCESS, "User created successfully")
          return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        user = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=user, password=password)

        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Wellcome back {user.username}')
            return HttpResponseRedirect(reverse('game:play'))
        else:
            messages.add_message(
                self.request, messages.ERROR, ('User not registered or wrong password'))
            return super(LoginView, self).form_invalid(form)
      

from django.shortcuts import render, redirect
from game.forms import LetterForm
from game.HangMan import (
    start_new_game,
    process_guess,
    get_display_word,
    is_game_over,
    did_win
)

#English
@login_required
def play_game(request):
    # Start a new game if not started
    if "hangman_game" not in request.session:
        request.session["hangman_game"] = start_new_game()

    game = request.session["hangman_game"]

    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.cleaned_data["letter"].lower()
            #updates the game state based on the guessed letter
            game = process_guess(game, letter)
            request.session["hangman_game"] = game
            return redirect("game:play")  # prevent form resubmission
    else:
        form = LetterForm()

    context = {
        "form": form,
        "word_display": get_display_word(game),
        "attempts": game["attempts"],
        "max_attempts": game["max_attempts"],
        "game_over": is_game_over(game),
        "won": did_win(game),
        "word": game["word"],
        "guessed_letters": game["guessed_letters"],
    }
    return render(request, "game/play.html", context)

def reset_game(request):
    if "hangman_game" in request.session:
        del request.session["hangman_game"]
    return redirect("game:play")


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Logout successfully")
    return HttpResponseRedirect(reverse('game:home'))

#Español
from game.forms import FormLetra
from game.ahorcado import (
    inicio,
    verificar,
    display_palabra,
    fin_juego,
    ganaste
)
@login_required
def jugar(request):
    # Start a new game if not started
    if "ahorcado" not in request.session:
        request.session["ahorcado"] = inicio()

    game = request.session["ahorcado"]

    if request.method == "POST":
        form = FormLetra(request.POST)
        if form.is_valid():
            letra = form.cleaned_data["letra"].lower()
            #updates the game state based on the guessed letter
            game = verificar(game, letra)
            request.session["ahorcado"] = game
            return redirect("game:jugar")  # prevent form resubmission
    else:
        form = FormLetra()

    context = {
        "form": form,
        "word_display": display_palabra(game),
        "attempts": game["intentos"],
        "max_attempts": game["max_intentos"],
        "game_over": fin_juego(game),
        "won": ganaste(game),
        "word": game["palabra"],
        "guessed_letters": game["letras_adivinadas"],
    }
    return render(request, "game/jugar.html", context)

def reset_juego(request):
    if "ahorcado" in request.session:
        del request.session["ahorcado"]
    return redirect("game:jugar")


@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Logout successfully")
    return HttpResponseRedirect(reverse('game:home'))
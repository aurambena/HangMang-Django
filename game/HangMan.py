import random

def start_new_game():
    data = []
    with open("./game/files/data.txt","r", encoding="utf-8") as f:
        for line in f:
            data.append(str(line))
            
    word = random.choice(data)
    
    return {
        "word": word,
        "guessed_letters": [],
        "attempts": 0,
        "max_attempts": 12
    }

def process_guess(game_state, letter):
    word = game_state["word"]
    guessed = game_state["guessed_letters"]

    if letter not in guessed:
        guessed.append(letter)
        if letter not in word:
            game_state["attempts"] += 1
    
    return game_state

def get_display_word(game_state):
    return [l if l in game_state["guessed_letters"] else "_ " for l in game_state["word"]]

def is_game_over(game_state):
    word = game_state["word"]
    return game_state["attempts"] >= game_state["max_attempts"] or all(l in game_state["guessed_letters"] for l in word)

def did_win(game_state):
    return all(l in game_state["guessed_letters"] for l in game_state["word"])
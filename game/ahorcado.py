import random

def inicio():
    data = []
    with open("./game/files/datos.txt","r", encoding="utf-8") as f:
        for line in f:
            data.append(str(line))
            
    palabra = random.choice(data)
    palabra = palabra[:-1]
    return {
        "palabra": palabra,
        "letras_adivinadas": [],
        "intentos": 0,
        "max_intentos": 12
    }

def verificar(estado_juego, letra):
    palabra = estado_juego["palabra"]
    guessed = estado_juego["letras_adivinadas"]

    if letra not in guessed:
        guessed.append(letra)
        if letra not in palabra:
            estado_juego["intentos"] += 1
    
    return estado_juego

def display_palabra(estado_juego):
    display = []
    for i in estado_juego["palabra"]:
        if i in estado_juego["letras_adivinadas"]:
            display.append(i)
        else:
            display.append("_ ")
    
    return display
   
def fin_juego(estado_juego, estadisticas_jugador):
    palabra = estado_juego["palabra"]
    return estado_juego["intentos"] >= estado_juego["max_intentos"] or all(l in estado_juego["letras_adivinadas"] for l in palabra)

def ganaste(estado_juego):
    return all(l in estado_juego["letras_adivinadas"] for l in estado_juego["palabra"])


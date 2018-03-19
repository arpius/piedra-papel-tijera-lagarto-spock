#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

PIEDRA = opciones[0]
PAPEL = opciones[1]
TIJERA = opciones[2]
LAGARTO = opciones[3]
SPOCK = opciones[4]

jugador = input("Hola forastero, ¿cómo te llamas?\n>> ")


def introduccion():
    print("\nEncantado de conocerte {}.".format(str.capitalize(jugador)))
    print("Vamos a jugar a piedra, papel, tijera, lagarto, Spock y si me ganas",
          "podrás irte a tu casa. Pero de lo contario...",
          "tendrás que casarte con mi prima. Si, aquella con bigote.")


def jugada_aleatoria():
    jugada = ''.join(choice(opciones))
    return jugada


def combate_a_muerte(jugador, contrincante):
    jugador = str.lower(jugador)
    contrincante = str.lower(contrincante)
    victoria = False

    if jugador == PIEDRA and contrincante == PAPEL or jugador == PAPEL and contrincante == PIEDRA:
        resultado = "Papel envuelve piedra"
    elif jugador == PIEDRA and contrincante == TIJERA or jugador == TIJERA and contrincante == PIEDRA:
        resultado = "Piedra rompe tijera"
    elif jugador == PIEDRA and contrincante == LAGARTO or jugador == LAGARTO and contrincante == PIEDRA:
        resultado = "Piedra aplasta lagarto"
    elif jugador == PIEDRA and contrincante == SPOCK or jugador == SPOCK and contrincante == PIEDRA:
        resultado = "Spock vaporiza piedra"
    elif jugador == PAPEL and contrincante == TIJERA or jugador == TIJERA and contrincante == PAPEL:
        resultado = "Tijera corta papel"
    elif jugador == PAPEL and contrincante == LAGARTO or jugador == LAGARTO and contrincante == PAPEL:
        resultado = "Lagarto come papel"
    elif jugador == PAPEL and contrincante == SPOCK or jugador == SPOCK and contrincante == PAPEL:
        resultado = "Papel refuta Spock"
    elif jugador == TIJERA and contrincante == LAGARTO or jugador == LAGARTO and contrincante == TIJERA:
        resultado = "Tijera decapita lagarto"
    elif jugador == TIJERA and contrincante == SPOCK or jugador == SPOCK and contrincante == TIJERA:
        resultado = "Spock desintegra tijera"
    elif jugador == SPOCK and contrincante == LAGARTO or jugador == LAGARTO and contrincante == SPOCK:
        resultado = "Lagarto envenena Spock"
    elif jugador == PIEDRA and contrincante == PIEDRA or \
            jugador == PAPEL and contrincante == PAPEL or \
            jugador == TIJERA and contrincante == TIJERA or \
            jugador == LAGARTO and contrincante == LAGARTO or \
            jugador == SPOCK and contrincante == SPOCK:
        resultado = "¡Empate! voy al rincón de llorar, espero" \
                    "que sigas ahí cuando vuelva..."
    else:
        resultado = "Ese movimiento no está permitido."

    if jugador == PIEDRA and contrincante == TIJERA or \
            jugador == PIEDRA and contrincante == LAGARTO or \
            jugador == PAPEL and contrincante == PIEDRA or \
            jugador == PAPEL and contrincante == SPOCK or \
            jugador == TIJERA and contrincante == PAPEL or \
            jugador == TIJERA and contrincante == LAGARTO or \
            jugador == LAGARTO and contrincante == PAPEL or \
            jugador == LAGARTO and contrincante == SPOCK or \
            jugador == SPOCK and contrincante == PIEDRA or \
            jugador == SPOCK and contrincante == TIJERA:
        victoria = True

    if victoria:
        return "{} ¡Maldición! he sido derrotado :(".format(resultado)
    else:
        return "{} ¡MWAJAJAJA te casarás con mi prima!".format(resultado)


introduccion()
turno = input("\nElige bien tus bazas. Es tu turno:\n>> ")
contrincante = jugada_aleatoria()

print("{} contra {}. ".format(str.upper(turno), str.upper(contrincante)))
print(combate_a_muerte(turno, contrincante))

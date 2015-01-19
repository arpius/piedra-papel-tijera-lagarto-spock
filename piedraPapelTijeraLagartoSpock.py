#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 17:40:37 2015

@author: aritz
"""
from random import choice

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
jugador = raw_input("Hola forastero, ¿cómo te llamas?\n>> ")

print "\nEncantado de conocerte %s." % str.capitalize(jugador)
print "\nVamos a jugar a piedra, papel, tijera, lagarto, Spock y si me ganas "
print "podrás irte a tu casa. Pero de lo contario..."
print "\n...tendrás que casarte con mi prima. Si, aquella con bigote."

turno = raw_input("\nElige bien tus bazas. Es tu turno:\n>> ")


def jugada_aleatoria():
    jugada = ''.join(choice(opciones))
    return jugada


def combate_a_muerte(jugador, contrincante):
    jugador = str.lower(jugador)
    contrincante = str.lower(contrincante)
    victoria = False
    if jugador == opciones[0] and contrincante == opciones[1]:
        resultado = "Papel envuelve piedra"
    elif jugador == opciones[0] and contrincante == opciones[2]:
        victoria = True
        resultado = "Piedra rompe tijera"
    elif jugador == opciones[0] and contrincante == opciones[3]:
        victoria = True
        resultado = "Piedra aplasta lagarto"
    elif jugador == opciones[0] and contrincante == opciones[4]:
        resultado = "Spock vaporiza piedra"
    elif jugador == opciones[1] and contrincante == opciones[0]:
        victoria = True
        resultado = "Papel envuelve piedra"
    elif jugador == opciones[1] and contrincante == opciones[2]:
        resultado = "Tijera corta papel"
    elif jugador == opciones[1] and contrincante == opciones[3]:
        resultado = "Lagarto come papel"
    elif jugador == opciones[1] and contrincante == opciones[4]:
        victoria = True
        resultado = "Papel refuta Spock"
    elif jugador == opciones[2] and contrincante == opciones[0]:
        resultado = "Piedra rompe tijera"
    elif jugador == opciones[2] and contrincante == opciones[1]:
        victoria = True
        resultado = "Tijera corta papel"
    elif jugador == opciones[2] and contrincante == opciones[3]:
        victoria = True
        resultado = "Tijera decapita lagarto"
    elif jugador == opciones[2] and contrincante == opciones[4]:
        resultado = "Spock desintegra tijera"
    elif jugador == opciones[3] and contrincante == opciones[0]:
        resultado = "Piedra aplasta lagarto"
    elif jugador == opciones[3] and contrincante == opciones[1]:
        victoria = True
        resultado = "Lagarto come papel"
    elif jugador == opciones[3] and contrincante == opciones[2]:
        resultado = "Tijera decapita lagarto"
    elif jugador == opciones[3] and contrincante == opciones[4]:
        victoria = True
        resultado = "Lagarto envenena Spock"
    elif jugador == opciones[4] and contrincante == opciones[0]:
        victoria = True
        resultado = "Spock vaporiza piedra"
    elif jugador == opciones[4] and contrincante == opciones[1]:
        resultado = "Papel refuta Spock"
    elif jugador == opciones[4] and contrincante == opciones[2]:
        victoria = True
        resultado = "Spock desintegra tijera"
    elif jugador == opciones[4] and contrincante == opciones[3]:
        resultado = "Lagarto envenena Spock"
    elif (jugador == opciones[0] and contrincante == opciones[0] or
            jugador == opciones[1] and contrincante == opciones[1] or
            jugador == opciones[2] and contrincante == opciones[2] or
            jugador == opciones[3] and contrincante == opciones[3] or
            jugador == opciones[4] and contrincante == opciones[4]):
        resultado = "¡Empate! voy al rincón de llorar, espero" \
                    " que sigas ahí cuando vuelva..."
    else:
        resultado = "Ese movimiento no está permitido."
    if victoria:
        return "%s ¡Maldición! he sido derrotado :(" % resultado
    else:
        return "%s ¡MWAJAJAJA te casarás con mi prima!" % resultado

contrincante = jugada_aleatoria()
print "%s contra %s. " % (str.upper(turno), str.upper(contrincante))
print combate_a_muerte(turno, contrincante)

# Librerias
import turtle
import os
from tkinter import *
from tkinter import messagebox

#import pygame
#pygame.init()
#pygame.mixer.init()

# sdf = pygame.mixer.Sound("fatality.wav")
# pygame.mixer.Sound.play(sdf, -1)

wn = turtle.Screen()
wn.title("Ping pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Inicialismos el puntaje en 0
puntuacionA = 0
puntuacionB = 0

# Mensaje de ganador


def msg(jugador):
    messagebox.showinfo("Ganador¡", "El Jugador " + jugador + " gana 🎇 🏓 🎇")
    quit()
    # root = Tk()
    # Button(root, text="Aquí", command=msg).pack()
    # root.mainloop()


# Posicion de inicio de las raquetas
RaquetaA = turtle.Turtle()
RaquetaA.speed(0)
RaquetaA.shape("square")
RaquetaA.color("white")
RaquetaA.shapesize(stretch_wid=5, stretch_len=1)
RaquetaA.penup()
RaquetaA.goto(-350, 0)

RaquetaB = turtle.Turtle()
RaquetaB.speed(0)
RaquetaB.shape("square")
RaquetaB.color("white")
RaquetaB.shapesize(stretch_wid=5, stretch_len=1)
RaquetaB.penup()
RaquetaB.goto(350, 0)

# Color del balon y posición inicial
Bola = turtle.Turtle()
Bola.speed(0)
Bola.shape("square")
Bola.color("white")
Bola.penup()
Bola.goto(0, 0)
Bola.dx = 1
Bola.dy = 1

# Texto de puntuacion
Linea = turtle.Turtle()
Linea.speed(0)
Linea.shape("square")
Linea.color("white")
Linea.penup()
Linea.goto(0, 200)
Linea.write("Jugador 1: 0, Jugador 2: 0", align="center",
            font=("Courier", 30, "normal"))

# Movimiento de jugadores


def RaquetaA_up():
    y = RaquetaA.ycor()
    if (y < 200):
        y += 40
        RaquetaA.sety(y)


def RaquetaA_down():
    y = RaquetaA.ycor()
    if (y > -240):
        y -= 40
        RaquetaA.sety(y)


def RaquetaB_up():
    y = RaquetaB.ycor()
    # print(y)
    if (y < 200):
        y += 40
        RaquetaB.sety(y)


def RaquetaB_down():
    y = RaquetaB.ycor()
    # print(y)
    if (y > -240):
        y -= 40
        RaquetaB.sety(y)


# Teclas de uso
wn.listen()  # estar alerta
wn.onkeypress(RaquetaA_up, 'w')  # al presionar se ejecuta
wn.onkeypress(RaquetaA_down, 's')
wn.onkeypress(RaquetaB_up, 'Up')
wn.onkeypress(RaquetaB_down, "Down")

# Bucle de juego
while True:
    wn.update()
    # Movimiento de la bola
    Bola.setx(Bola.xcor() + Bola.dx)
    Bola.sety(Bola.ycor() + Bola.dy)

    # Fronteras
    # Arriba y abajo bola choque con sonido
    if Bola.ycor() > 290:
        Bola.sety(290)
        Bola.dy *= -1
        # incluir sonido
        # os.system("afplay sonido.wav&")
    elif Bola.ycor() < -290:
        Bola.sety(-290)
        Bola.dy *= -1
        # incluir sonido
        # os.system("afplay sonido.wav&")
    # Puntuación jugador A
    if Bola.xcor() > 350:
        puntuacionA += 1
        Bola.goto(0, 0)
        Bola.dx *= -1
        if puntuacionA < 9:
            Linea.clear()
            Linea.write("Jugador A: {} Jugador B {}".format(
                puntuacionA, puntuacionB), align="center", font=("Courier", 26, "normal"))
        else:
            jugador = "A"
            msg(jugador)
    # Puntuación jugador A
    if Bola.xcor() < -350:
        puntuacionB = puntuacionB + 1
        Bola.goto(0, 0)
        Bola.dx *= -1
        #print(puntuacionB)
        if puntuacionB == 10:
            jugador = "B"
            msg(jugador)
        else:
            Linea.clear()
            Linea.write("Jugador A: {} Jugador B {}".format(
                puntuacionA, puntuacionB), align="center", font=("Courier", 26, "normal"))
     # Raqueta y bolaw
    if Bola.xcor() < -340 and Bola.ycor() < RaquetaA.ycor() + 50 and Bola.ycor() > RaquetaA.ycor() - 50:
        Bola.dx *= -1
        # playsound('sonido.wav')

    elif Bola.xcor() > 340 and Bola.ycor() < RaquetaB.ycor() + 50 and Bola.ycor() > RaquetaB.ycor() - 50:
        Bola.dx += -1
        # playsound('sonido.wav')

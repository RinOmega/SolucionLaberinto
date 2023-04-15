#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Laberinto import Laberinto


class Juego:
    
    def __init__ (self):
        self.laberinto=None
        

    def fabricarLaberinto():
        return Laberinto()

    def laberinto2HabitacionesFM(self):
        abierta=True
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuertaLado1Lado2(abierta,hab1, hab2)
        
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()
        
        hab2.sur = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()
        
        hab1.sur = puerta
        hab2.norte = puerta
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)



    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        return hab

    def fabricarPuertaLado1Lado2(self,abierta, unaHab, otraHab):
        puerta = Puerta(abierta,lado1=unaHab,lado2=otraHab)
        return puerta

    def fabricarPared(self):
        return Pared()

    
unjuego=Juego()
unjuego.fabricarLaberinto()
unjuego.laberinto2HabitacionesFM()
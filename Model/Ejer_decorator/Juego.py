#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Laberinto import Laberinto
from Baul import Baul
from Espada import Espada
from Bomba import Bomba
from Fuego import Fuego

class Juego:
    
    def __init__(self):
        self.laberinto=None
        
    def fabricarLaberinto(self):
        return Laberinto()

    def laberinto2HabitacionesFM(self):
        self.laberinto = self.fabricarLaberinto()

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
    
    def fabricarBaulEn(self,cont):
        num = len(cont.hijos)
        baul = Baul(num)
        cont.agregarHijo(baul)
    
    def fabricarEspadaEn(self,cont):
        espada = Espada()
        cont.agregarHijo(espada)
    
    def fabricarBombaEn(self,cont):
        bomba = Bomba()
        cont.agregarHijo(bomba)
    
    def laberinto4Habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        abierta=True
        abierta2=False
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        fuego = Fuego()
        fuego.decorar(hab4)

        puerta1 = self.fabricarPuertaLado1Lado2(abierta,hab1, hab2)
        puerta4 = self.fabricarPuertaLado1Lado2(abierta2,hab1, hab3)
        puerta2 = self.fabricarPuertaLado1Lado2(abierta,hab2, hab4)
        bombaP=Bomba()
        puerta3 = self.fabricarPuertaLado1Lado2(abierta,hab3, hab4)
        bombaP.decorar(puerta3)
        
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.sur = puerta4
        hab1.este = puerta1

        hab2.norte = self.fabricarPared()
        hab2.este = self.fabricarPared()
        hab2.oeste = puerta1
        hab2.sur = puerta2
        baul2=self.fabricarBaulEn(hab2)
        self.fabricarBombaEn(baul2)

        hab3.norte = puerta4
        hab3.oeste= self.fabricarPared()
        hab3.sur=self.fabricarPared()
        hab3.este=puerta3
        baul3=self.fabricarBaulEn(hab3)
        self.fabricarEspadaEn(baul3)

        hab4.norte=puerta2
        hab4.este=self.fabricarPared()
        hab4.sur=self.fabricarPared()
        hab4.oeste=puerta3

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)



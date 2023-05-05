#!/usr/bin/python
#-*- coding: utf-8 -*-

class Laberinto:
    def __init__(self):
        self.habitaciones = []
        return self
    
    def habitaciones(self):
        return self.habitaciones

    def agregarHabitacion(self, unaHab):
        self.habitaciones.append(unaHab)
        
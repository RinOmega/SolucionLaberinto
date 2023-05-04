#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.num=num
        self.norte=None
        self.este=None
        self.oeste=None
        self.sur=None

    def entrar(self):
        print('Estas en la habitacion', str(self.num))

    #def get_este():
    #    global este
     #   return este
    

    #def get_norte():
   #     global norte
    #    return norte
    
   # def get_sur():
    #    global sur
    #    return sur
    
   # def get_oeste():
    #    global oeste
    #    return oeste
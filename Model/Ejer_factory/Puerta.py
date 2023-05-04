#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self,abierta,lado1,lado2):
        self.abierta = abierta
        self.lado1 = lado1
        self.lado2 = lado2
    
    def abierta(self):
        return self.abierta

    def lado1(self):
        return self.lado1


    def lado2(self):
        return self.lado2

        
    def entrar(self):
        print('La puerta está cerrada')
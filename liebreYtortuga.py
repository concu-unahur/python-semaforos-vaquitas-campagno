import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

#semaVaca = threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = 0.5

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):

      #if (inicioPuente-1 == self.posicion):
      #      semaVaca.acquire()
      
      #if (30 == self.posicion):
      #      semaVaca.release()


      self.avanzar()

class Tortuga(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = 1

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐢")

  def run(self):
    while(True):

      #if (inicioPuente-1 == self.posicion):
      #      semaVaca.acquire()
      
      #if (30 == self.posicion):
      #      semaVaca.release()


      self.avanzar()

class Liebre(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = 0.08

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐇")

  def run(self):
    while(True):

      #if (inicioPuente-1 == self.posicion):
      #      semaVaca.acquire()
      
      #if (30 == self.posicion):
      #      semaVaca.release()


      self.avanzar()

vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

tortugas = []
for i in range(1):
  t = Tortuga()
  tortugas.append(t)
  t.start()  

liebres = []
for i in range(2):
  l = Liebre()
  liebres.append(l)
  l.start()  



def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()

  for v in vacas:
    v.dibujar()
  
  for t in tortugas:
    t.dibujar()

  for l in liebres:
    l.dibujar()

  dibujarPuente()
  time.sleep(0.2)
"""
@author: Christopher Oswaldo Márquez Reyes
@author: Valeria Marian Andrade Monreal
"""

import heapq
import sys
import time


# ---------------------------- Clases del código --------------------------------------------------------
class Mapa:
    def __init__(self, pos_actual):
        self.matriz = [[2, 5, 1, 7],
                       [13, 8, 11, 10],
                       [6, 9, 10, 8],
                       [12, 3, 1, 7]]
        self.pos_actual = pos_actual

    def calcular_min_costo(self, destino):
        m = len(self.matriz)
        n = len(self.matriz[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # derecha, izquierda, abajo, arriba

        dp[self.pos_actual[0]][self.pos_actual[1]] = self.matriz[self.pos_actual[0]][self.pos_actual[1]]
        heap = [(dp[self.pos_actual[0]][self.pos_actual[1]], self.pos_actual)]

        while heap:
            costo_actual, (i, j) = heapq.heappop(heap)

            if costo_actual != dp[i][j]:
                continue

            for dx, dy in movimientos:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n:
                    costo_nuevo = costo_actual + self.matriz[x][y]

                    if costo_nuevo < dp[x][y]:
                        dp[x][y] = costo_nuevo
                        heapq.heappush(heap, (costo_nuevo, (x, y)))

        min_costo = dp[destino[0]][destino[1]]
        return min_costo

    # Determinamos las coordenadas de cada lugar en el mapa
    def obtener_posicion_lugar(self, lugar):
        lugares = {
            'Lugar1': (3, 0),
            'Lugar2': (0, 1),
            'Lugar3': (0, 2),
            'Lugar4': (0, 3),
            'Lugar5': (1, 0),
            # Añade más lugares según sea necesario
        }
        return lugares.get(lugar)


# Inicializamos los atributos del personaje principal
class Player:
    def __init__(self, name='', hp=100, location=(0, 0), status_effects=None, items=None, money=0, bulletproof = False, gun = False, weapons = []):
        self.name = name
        self.weapons = weapons if weapons is not None else []
        self.bulletproof = bulletproof
        self.gun = gun
        self.hp = hp
        self.location = location
        self.status_effects = status_effects if status_effects is not None else []
        self.items = items if items is not None else []
        self.money = money
        self.mapa = Mapa(location)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    
    def get_weapons(self):
        for weapon in self.weapons:
            print(f"\n    - {weapon}\n")

    # Imprimimos la lista de items
    def get_items(self):
        return self.items

    # Agregamos un item al inventario
    def add_item(self, item):
        self.items.append(item)

    # Agregamos dinero al inventario
    def add_money(self, money):
        self.money += money

    # Actualizamos la posición del jugador en tiempo real
    def mover(self, nueva_posicion):
        self.location = nueva_posicion
        self.mapa.pos_actual = nueva_posicion


myPlayer = Player()

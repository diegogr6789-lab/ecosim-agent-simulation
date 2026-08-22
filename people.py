import random

class poblacion():
    def __init__(self, nombre):
        self.destino = None
        self.pos = [0,0]
        self.traveling = False
        self.age = 0
        self.money = 0
        self.hambre = 100
        self.nombre = nombre
        self.tipo = random.choice([
            "Ahorrador",#buy when the market is cheap
            "Impulsivo",#buy as soon he has money
            "Emprendedor",#buy cheap and go to other cities to sell more expensive
            "Granjero",#produce and eat some part of it
            
        ])
        if self.tipo == "Granjero":
            self.stock = 0
    

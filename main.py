from ciudades import ciudad
from people import poblacion
import math
import pygame
import time
import random

pygame.init()
fuente = pygame.font.SysFont("Arial", 25)

screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

def new():
    name = ""
    for j in range(random.randint(3,7)):
                name += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    return poblacion(name)

def draw_dashed_line(surf, color, start_pos, end_pos, dash_length=10, space_length=5, width=5):
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    dist_total = math.hypot(x2 - x1, y2 - y1)
    angle = math.atan2(y2 - y1, x2 - x1)
    
    margin = 30
    step = dash_length + space_length
    
    for d in range(margin, int(dist_total - margin), step):
        start = (x1 + math.cos(angle) * d, 
                 y1 + math.sin(angle) * d)
        
        end_d = min(d + dash_length, dist_total - margin)
        end = (x1 + math.cos(angle) * end_d, 
               y1 + math.sin(angle) * end_d)
        
        pygame.draw.line(surf, color, start, end, width)


def newPerson():
    name = ""
    npersonas = 0
    for city in ciudades:
        npersonas += city["Cciudadanos"]
    spawn = random.randint(0,math.ceil(npersonas/3))
    place = random.randint(0,len(ciudades)-1)

    stock = 0
    for city in ciudades:
        stock += city["stock"]

    for i in range((int(stock/100))):
            for j in range(random.randint(3,7)):
                name += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
            
            
            if spawn >= 1:
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
            if spawn >= 10:
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
            if spawn >= 50:
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
            if spawn >= 200:
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
                persona = new()
                ciudades[place]["ciudadanos"].append(persona)
                ciudades[place]["Cciudadanos"] += 1
    print(npersonas)

def display():
    if len(ciudades) > 1:
        for i in range(len(ciudades)):
            for j in range(len(ciudades)-1):
                cord1 = (ciudades[i]["posicion"][0],ciudades[i]["posicion"][1])
                cord2 = (ciudades[j]["posicion"][0],ciudades[j]["posicion"][1])
                draw_dashed_line(screen,(255,255,0),cord1,cord2)
    
    for city in ciudades:
            cord1 = (city["posicion"][0],city["posicion"][1])
            pygame.draw.circle(screen, (0, 255, 0), cord1, 50)

            texto1 = fuente.render(city["nombre"], True, (0,0,0))
            recttexto1 = texto1.get_rect()
            recttexto1.center = city["posicion"] 
            screen.blit(texto1, recttexto1)

            if not city["Cciudadanos"] >= 1000:
                texto2 = fuente.render(str(city['Cciudadanos']), True, (0, 0, 0))
            elif city["Cciudadanos"] >= 1000:
                texto2 = fuente.render(str(f"{math.floor(city['Cciudadanos']/1000)}K"), True, (0, 0, 0))
            elif city["Cciudadanos"] >= 1000000:
                texto2 = fuente.render(str(f"{math.floor(city['Cciudadanos']/1000000)}M"), True, (0, 0, 0))

            cord2 = (city["posicion"][0]-5,city["posicion"][1]+15)
            screen.blit(texto2, cord2)
            
            if not city["stock"] >= 1000:
                texto = city["stock"]
            elif city["stock"] >= 1000:
                texto = f"{math.floor(city['stock']/1000)}K"
            elif city["stock"] >= 1000000:
                texto = f"{math.floor(city['stock']/1000000)}M"

            text = f"{city['precio']}€ {texto}"
            texto2 = fuente.render(text, True, (0, 0, 0))
            cord2 = (city["posicion"][0]-40,city["posicion"][1]-35)
            screen.blit(texto2, cord2)

def actualizar_precios():
    for city in ciudades:
        nciudadanos = city["Cciudadanos"]
        stock = city["stock"]
        if stock > 0:
            precio = 10 * (nciudadanos / stock)
            city["precio"] = max(2, round(precio, 2))
        else:
            city["precio"] = 100   

def emprender(people,cord):
    people.pos = list(cord)
    precios = []
    for city in ciudades:
        if city["posicion"] == cord:
            place = city
    x1, y1 = place["posicion"]
    
    for city in ciudades:
        x2, y2 = city["posicion"]
        distancia = math.hypot(x2 - x1, y2 - y1)
        nuevaCity = {
            "posicion":city["posicion"],
            "precio": city["precio"],
            "distancia": round(distancia/10),
            "ganancia": 2*round(distancia/10)-city["precio"]
        }
        if city["posicion"] == place["posicion"]:
            qcity = nuevaCity
        precios.append(nuevaCity)
    precios.remove(qcity)

    destino = min(precios, key=lambda city: city["ganancia"])
    
    if destino["distancia"] < people.money:
        people.destino = destino
        people.traveling = True





def eat(people,city):
    if people.money - city['precio'] >= 0 and city["stock"] > 0:
        people.money -= city['precio']
        people.hambre += random.randint(2,5)
        city["stock"] -= 1
    

for i in range(5):
    name = ""
    for i in range(random.randint(5,8)):
        name += random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    madrid = ciudad(random.randint(50,950),random.randint(50,950),name)

ciudades = ciudad.city()

while True:
    screen.fill((30, 30, 30))
    
    display()
    newPerson()
    actualizar_precios()

    for city in ciudades:
        for people in city["ciudadanos"]:
            people.hambre -= random.randint(0,2)
            people.age += 1
            people.money += random.randint(1,5)
            if people.hambre <= 0 :
                city["ciudadanos"].remove(people)
                city["Cciudadanos"] -= 1
            

            if people.tipo == "Ahorrador":
                if city['precio'] <= 3 or people.hambre <= 25:
                    eat(people,city)


            elif people.tipo == "Impulsivo":
                if city['precio'] <= people.money:
                    eat(people,city)


            elif people.tipo == "Emprendedor":
                if city['precio'] <= 5 or people.hambre <= 25:
                    eat(people,city)

                if people.traveling == False:
                    cord1 = (random.randint(city["posicion"][0]-25,city["posicion"][0]+25),random.randint(city["posicion"][1]-25,city["posicion"][1]+25))
                    cord = (city["posicion"][0],city["posicion"][1])
                    emprender(people,cord)
                else:
                    people.hambre -= 1
                    x = False
                    y = False

                    destino = people.destino["posicion"]
                    velocidad = 7.5

                    if people.pos[0] < destino[0]:
                        people.pos[0] += velocidad
                    elif people.pos[0] > destino[0]:
                        people.pos[0] -= velocidad
                    
                    elif people.pos[0] == destino[0]:
                        x = True

                    if people.pos[1] < destino[1]:
                        people.pos[1] += velocidad
                    elif people.pos[1] > destino[1]:
                        people.pos[1] -= velocidad

                    elif people.pos[0] == destino[0]:
                        y = True

                    if x and y:
                        people.money += people.destino["precio"]
                        city["stock"] -= 1
                        people.money -= people.destino["distancia"]
                        people.traveling = False


                    pygame.draw.circle(screen, (255, 0, 0), people.pos, 5)


            elif people.tipo == "Granjero":
                people.stock += random.randint(0,2)
                if people.hambre <= 25:
                    if city['precio'] <= 5 or people.hambre <= 25:
                        eat(people,city)
                if people.stock > 0:

                        people.money += city['precio']
                        people.stock -= 1
                        city["stock"] += 1

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()
    time.sleep(0.5)
    clock.tick(60)
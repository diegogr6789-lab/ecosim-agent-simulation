cities = []

class ciudad():
    def __init__(self,cordX,cordY,name):
        self.position = (cordX,cordY)
        self.name = name
        

        nuevaCity = {
            "nombre": self.name,
            "posicion": self.position,
            "ciudadanos": [], 
            "Cciudadanos": 1,
            "stock": 100,
            "precio": 0
        }
        cities.append(nuevaCity)

    def city():
        return cities
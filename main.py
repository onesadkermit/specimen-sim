import os
#==========блок функций==============
def menu_print():
    """печать меню действий в консоль
    """
    print("1 - create new environment")
    print("2 - create new spiceman")
    print("3 - populate selected environment")
    print("4 - exit")

def create_environment():
    global environment
    environment = Environment("new_env")
    print()

def create_spiceman():
    print()

def populate_environment(count):
    #environment = []
    for i in range(count):
        environment.objList.append(PhysObj(Point(0, 0, 0),Figure(),i))
    print()
#==========блок классов===============

class Point:
    def __init__(self, x: float, y: float, z:float):
        self._x = x
        self._y = y
        self._z = z

class Figure:
    def __init__(self, form = "None"):
        self.currForm = "None"
        self.verticles = []
        self.r = 0

    def setCenterPoint (self, point: Point):
        self.centerPoint = point

    def convToCube(self, verticle: Point):
        self.currForm = "Cube"
        if hasattr(self, "r"):
            del self.r
        self.verticles = [verticle]

    def convToSphere(self, r: float):
        self.currForm = "Sphere"
        if hasattr(self, "verticles"):
            del self.verticles     

    def convToTetra(self, verticle: Point):
        self.currForm = "Tetra"
        if hasattr(self, "r"):
            del self.r
        self.verticles = [verticle]

    #if здес написать ини конвертер в форму из дефолтной
        
class PhysObj:
    def __init__(self, centerPoint: Point(0, 0, 0), figure: Figure(), objId: int):
        self.figure = figure
        self.figure.setCenterPoint(centerPoint)
        self.objId = objId
    
class Environment:
    def __init__(self, name = "None"):
        self.name = name
        self.objList = []
#==========исполняемый блок===========
get_ch = 0
while not(get_ch == "4"):
    menu_print()
    get_ch = input()
    match get_ch:
        case "1":
            create_environment()
        case "2":
            create_spiceman()
        case "3":
            print("введите количество")
            count = input()
            populate_environment(int(count))
        case "4":
            print("выход")
        case _:
            print("выберите пункт меню")
    



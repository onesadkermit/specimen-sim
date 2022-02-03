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
    print()

def create_spiceman():
    print()

def populate_environment():
    print()
#==========блок классов===============

class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        
    @property
    def x(self): 
        print('Getting x') 
        return self._x    

    @x.setter
    def x(self, x): 
        print('Setting x to ' + x) 
        self._x = x

class Figure:
    def __init__(self):
      pass
    def setCenterPoint (self, x, y, z):
        self.centerPoint = Point(x, y, z)

#==========исполняемый блок===========
get_ch = 0
while not(get_ch == "4"):
    menu_print()
    get_ch = input();
    match get_ch:
        case "1":
           create_environment()
        case "2":
           create_spiceman()
        case "3":
           populate_environment()
        case "4":
           print("выход")
        case _:
           print("выберите пункт меню")
    



import csv
import datetime

class PIZZA:
    def __init__(self):
        self.description = "Unknown Pızza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
class Klasik_Pızza(PIZZA):
    def _init_(self):
        super()._init_()
        self.description = "KLASİK PIZZA"
        self.cost = 10.0
class MARGARİTA_PIZZA(PIZZA):
    def _init_(self):
        super()._init_()
        self.description = "MARGARİTA PIZZA"
        self.cost = 12.0  
class TÜRK_PIZZA(PIZZA):
    def _init_(self):
        super()._init_()
        self.description = "TÜRK PIZZA"
        self.cost = 15.0        
class SADE_PIZZA(PIZZA):
    def _init_(self):
        super()._init_()
        self.description = "SADE PIZZA"
        self.cost = 8.0    
class Decorator(PIZZA):
    def __init__(self, component):
        super().__init__()
        self.component = component
        def get_cost(self):
            return self.component.get_cost() + super().get_cost()

        def get_description(self):
            return self.component.get_description() + " " + super().get_description()
class ZEYTİN(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "ZEYTIN"
        self.cost = 2.0

class MANTAR(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "MANTAR"
        self.cost = 3.0

class KECI_PEYNIRI(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "KECI PEYNIRI"
        self.cost = 4.0

class ET(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "ET"
        self.cost = 5.0

class SOĞAN(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "SOĞAN"
        self.cost = 1.0

class MISIR(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "MISIR"
        self.cost = 2.5
def main():
    menu_file=open("menu.txt","r")
    menu_lines = menu_file.readlines()
    menu_file.close()
    
    print("MENU")
    for line in menu_lines:
        print(line.strip())
        
    pızza_seçımı= int(input("Lutfen bır pızza seçınız: "))
    sos_seçımı= int(input("Lutfen bır pızza seçınız: "))
    
    if pızza_seçımı == 1:
        pizza = Klasik_Pızza()
    elif pızza_seçımı == 2:
        pizza = MARGARİTA_PIZZA()
    elif pızza_seçımı == 3:
        pizza = TÜRK_PIZZA()
    else:
        print("Tekrar pızza secınız.")
        return

    if sos_seçımı == 11:
        pizza = ZEYTİN(pizza)
    elif sos_seçımı == 12:
        pizza = MANTAR(pizza)
    elif sos_seçımı == 13:
        pizza = KECI_PEYNIRI(pizza)
    elif sos_seçımı == 14:
        pizza = ET(pizza)
    elif sos_seçımı == 15:
        pizza = SOĞAN(pizza)
    elif sos_seçımı == 16:
        pizza = MISIR(pizza)
    else:
        print("Tekrar sos secınız.")
        return

    toplam_tutar = pizza.get_cost()

    print("Total cost:", toplam_tutar)
    
   isim = input("isminizi giriniz:")
    tc = input("tcnizi giriniz:")
    
    
                 
            
    
    
    
    

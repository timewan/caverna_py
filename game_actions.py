# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:48:37 2016

@author: TimeWanes
"""

class Action:
    def __init__(self, name, accum1, accum2, pickp):
        self.name = name
        self.acc1 = accum1
        self.acc2 = accum2
        self.pickup = pickp
        self.inv = {}
#       self.inv = {"Wood":0,"Stone":0,"Ore":0,"Rubies":0,"Grain":0, "Vegetable":0,"Gold Coins":0,"Food":0,"Dwarves":0,"Dogs":0,"Sheep":0,"Mule":0,"Boar":0,"Cattle":0}
            
    def update(self, items):
        for item in iter(items):
            if item in self.inv:
                self.inv[item] += items[item]
            else:
                self.inv[item] = items[item]
            
    def clear_inv(self):
        self.inv = {}
#        self.inv = {"Wood":0,"Stone":0,"Ore":0,"Rubies":0,"Grain":0, "Vegetable":0,"Gold Coins":0,"Food":0,"Dwarves":0,"Dogs":0,"Sheep":0,"Mule":0,"Boar":0,"Cattle":0}
        
        
        
drift_mining = Action("Drift Mining", {"Stone":1},{"Stone":1},{})
logging = Action("Logging",{"Wood":3},{"Wood":1},{})
wood_gathering = Action("Wood Gathering",{"Wood":1},{"Wood":1},{})
excavation = Action("Excavation",{"Stone":1},{"Stone":1},{})
supplies = Action("Supplies",{},{},{"Wood":1,"Stone":1,"Ore":1,"Food":1,"Gold Coins":2})
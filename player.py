# -*- coding: utf-8 -*-
import game_defs as gd


class Player:
    def __init__(self, name, dwarves):
        self.name = name
        self.dwarves = dwarves
        self.inv = {"Wood":0,"Stone":0,"Ore":0,"Rubies":0,"Grain":0, "Vegetable":0,"Gold Coins":0,"Food":1,"Dwarves":0,"Dogs":0,"Sheep":0,"Mule":0,"Boar":0,"Cattle":0}
    
    def add_items(self, items):
        for item in iter(items):
            self.inv[item] += items[item]
            
    def print_inv(self):
        print'Player Inventory || \n__________^______^^'
        for item in iter(self.inv):
            if (self.inv[item] > 0):
                print '{0:10}| {1:4d} ||'.format(item, int(self.inv[item]))
        return
        
        

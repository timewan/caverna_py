""" This file created 7/12/2016
    By: @timewanes
    Content: Def of classes for some Caverna Calculations """
    
import numpy as np


class GameData:
    inv_key = ["Wood","Stone","Ore","Rubies","Grain",
                "Vegetable","Gold Coins","Food","Dwarves",
                "Dogs","Sheep","Mule","Boar","Cattle"]
    tile_key = ["Empty", "Tunnel", "Cavern", "Plow", "Field", "Room"]
    turn = 0;
    
class Player:
    inv = np.zeros(14)
    score = 0;
    
class Board:
    tiles= np.zeros((8,6))
    t_points= np.zeros((8,6))
    


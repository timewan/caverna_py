# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:32:38 2016

@author: TimeWanes
"""
from PIL import Image, ImageDraw
import game_defs as gd

t_sz = 32
b = 3

def Draw_Out(coord,board, img):
    val = board.tiles[coord]    
    
    if (val==0):
        img.rectangle([ coord[0]*t_sz, coord[1]*t_sz, (coord[0]+1)*t_sz-1,
                       (coord[1]+1)*t_sz-1], fill=(40,255,40))
        img.rectangle([ coord[0]*t_sz+b, coord[1]*t_sz+b, (coord[0]+1)*t_sz-1-b,
                       (coord[1]+1)*t_sz-1-b], fill=(40,180,40))
    return
    
def Draw_In(coord, board, img):
    val = board.tiles[coord]
    
    if(val==0):
        img.rectangle([ coord[0]*t_sz, coord[1]*t_sz, (coord[0]+1)*t_sz-1,
                       (coord[1]+1)*t_sz-1], fill=(120,120,120))
        img.rectangle([ coord[0]*t_sz+b, coord[1]*t_sz+b, (coord[0]+1)*t_sz-1-b,
                       (coord[1]+1)*t_sz-1-b], fill=(20,20,20))
                    
    return





def Board_Picture(Board):
    image = Image.new('RGB',(8*t_sz,6*t_sz),(0,0,0))
    img = ImageDraw.Draw(image)    
    
    for y in range(0,5):
        for x in range(0,4):
            Draw_Out( (x,y), Board, img)
        for x in range(4,8):
            Draw_In( (x,y), Board, img)
        
    image.save('Board_shot.png')
    
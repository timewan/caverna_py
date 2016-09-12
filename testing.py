# -*- coding: utf-8 -*-

import game_defs as gd
import game_funcs as gf
import game_render as gr
import player
import game_actions as act


inv = {"Wood":2,"Stone":1,"Ore":0,"Rubies":0,"Grain":0,
       "Vegetable":0,"Gold Coins":0,"Food":1,"Dwarves":0,
       "Dogs":0,"Sheep":0,"Mule":0,"Boar":0,"Cattle":0}
       
       
Tim = player.Player("tim",2)      
Tim.add_items({"Wood":2})
       
Tim.print_inv()

availiable_actions = [act.drift_mining, act.logging, act.wood_gathering, act.supplies, act.excavation]
unavailiable_actions = []

for actions in availiable_actions:
    actions.update(actions.acc1)

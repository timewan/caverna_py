# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import game_defs as gd


def Print_Inv(player):
    game = gd.GameData()
    print'Player Inventory || \n__________^______^^'
    for i in range(0,13):
        if (player.inv[i] > 0):
            print '{0:10}| {1:4d} ||'.format(game.inv_key[i], int(player.inv[i]))
    return
    
    
    





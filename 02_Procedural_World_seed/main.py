#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2019 seth <seth@Deeper>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from seed import generate_seed
from make_noise import simplex, randomly_populate_map
from render_engine import *

w = 150
h = 100
class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        #by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight
 
def make_map(seed):
    global map
    #global seed
 
    #fill map with "unblocked" tiles
    map = [
         [Tile(False) for y in range(h)]
         for x in range(w) 
    ]
    print('seed : %s' % seed.__dict__)
    """
    for hello as 3537
    seed : {
    '_perm': [73, 3, 126, 39, 167, 225, 13, 62, 71, 77, 171, 81, 19, 23, 50, 134, 133, 174, 69, 98, 83, 35, 37, 170, 117, 90, 112, 151, 198, 240, 131, 136, 153, 197, 99, 157, 11, 87, 15, 57, 33, 45, 130, 47, 89, 109, 159, 164, 105, 208, 118, 181, 220, 226, 29, 246, 201, 86, 94, 0, 176, 193, 142, 228, 178, 146, 113, 163, 9, 150, 189, 152, 63, 196, 250, 192, 41, 74, 211, 183, 115, 38, 85, 209, 51, 54, 206, 97, 5, 82, 255, 4, 75, 128, 26, 111, 7, 103, 93, 186, 24, 119, 27, 36, 17, 6, 114, 195, 145, 253, 59, 234, 243, 213, 244, 125, 25, 237, 210, 165, 173, 179, 166, 187, 95, 216, 168, 175, 66, 137, 143, 135, 236, 219, 129, 227, 43, 149, 12, 248, 203, 28, 229, 249, 72, 40, 123, 224, 215, 205, 91, 199, 223, 18, 252, 222, 107, 242, 21, 84, 161, 241, 10, 254, 55, 232, 2, 207, 53, 78, 49, 132, 251, 188, 30, 191, 34, 182, 147, 200, 61, 70, 245, 20, 67, 217, 202, 56, 162, 8, 127, 233, 101, 44, 190, 96, 58, 204, 185, 92, 235, 42, 140, 156, 14, 218, 138, 239, 238, 144, 1, 120, 230, 110, 141, 247, 139, 122, 221, 104, 158, 154, 124, 148, 155, 184, 169, 108, 177, 22, 102, 172, 100, 52, 194, 16, 121, 214, 65, 68, 160, 106, 76, 88, 31, 64, 79, 60, 48, 116, 212, 80, 32, 46, 231, 180], 
    '_perm_grad_index_3D': [3, 9, 18, 45, 69, 27, 39, 42, 69, 15, 9, 27, 57, 69, 6, 42, 39, 18, 63, 6, 33, 33, 39, 6, 63, 54, 48, 21, 18, 0, 33, 48, 27, 15, 9, 39, 33, 45, 45, 27, 27, 63, 30, 69, 51, 39, 45, 60, 27, 48, 66, 39, 12, 30, 15, 18, 27, 42, 66, 0, 24, 3, 66, 36, 30, 6, 51, 57, 27, 18, 63, 24, 45, 12, 30, 0, 51, 6, 57, 45, 57, 42, 39, 51, 9, 18, 42, 3, 15, 30, 45, 12, 9, 24, 6, 45, 21, 21, 63, 54, 0, 69, 9, 36, 51, 18, 54, 9, 3, 39, 33, 54, 9, 63, 12, 15, 3, 63, 54, 63, 15, 33, 66, 57, 69, 0, 0, 21, 54, 51, 69, 45, 60, 9, 27, 33, 57, 15, 36, 24, 33, 12, 39, 27, 0, 48, 9, 24, 69, 39, 57, 21, 21, 54, 36, 18, 33, 6, 63, 36, 51, 3, 30, 42, 21, 48, 6, 45, 15, 18, 3, 36, 33, 60, 18, 69, 30, 42, 9, 24, 39, 66, 15, 60, 57, 3, 30, 24, 54, 24, 21, 51, 15, 60, 66, 0, 30, 36, 51, 60, 57, 54, 60, 36, 42, 6, 54, 69, 66, 0, 3, 0, 42, 42, 63, 21, 57, 6, 15, 24, 42, 30, 12, 12, 33, 48, 3, 36, 27, 66, 18, 12, 12, 12, 6, 48, 3, 66, 51, 60, 48, 30, 12, 48, 21, 48, 21, 36, 0, 60, 60, 24, 24, 66, 45, 36]
    }

    """
    #, octa=1, frequ=16.0
    #octa = seed.__dict__['_perm_grad_index_3D'][0]/seed.__dict__['_perm_grad_index_3D'][2]
    #freq = seed.__dict__['_perm_grad_index_3D'][1]/seed.__dict__['_perm_grad_index_3D'][3]
    
    div = seed.__dict__['_perm'][2]
    div2 = seed.__dict__['_perm'][0]
    
    if div == 0:
        div = 1
    if div2 == 0:
        div2 = 1
    octa = seed.__dict__['_perm'][0]*1/div#*seed.__dict__['_perm'][4]*2
    print('octa : %s ' % octa)
    freq = seed.__dict__['_perm'][1]*1/div2#*seed.__dict__['_perm'][3]*2
    print('freq : %s ' % freq)
    if octa == 0.0:
        octa = 1.0
    
    map = randomly_populate_map(map,seed, (w,h),octa,freq)
    #map = randomly_populate_map(map,seed, (w,h,1.2,6.0)) # ,1.2,6.0
    return map
 
    #place two pillars to test the map
    """
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[10][22].blocked = True
    map[10][22].block_sight = True
    map[11][22].blocked = True
    map[11][22].block_sight = True
    """


def main(args):
    global seed
    msg = 'mySeed : %s'
    try:
        mySeed = args[1]
    except:
        mySeed = 25
    if mySeed == 25:
        msg = 'The Default mySeed : %s'
    print(msg % mySeed)
    seed = generate_seed(mySeed)
    #print(args['seed'])
    global h
    global w
    #h = 3
    #w = 3
    
    
    #display_map(map)
    #generate map (at this point it's not drawn to the screen)
    map = make_map(seed)
    
    print(repr(map))
     
     
    #render the screen
    render_all(map)
    while not libtcod.console_is_window_closed():
     
     
        libtcod.console_flush()
     
        #erase all objects at their old locations, before they move
        for object in objects:
            object.clear()
     
        #handle keys and exit game if needed
        exit = handle_keys()
        if exit:
            break
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

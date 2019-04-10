import tcod as libtcod
from main import *
import random
#actual size of the window
SCREEN_WIDTH = w+30
SCREEN_HEIGHT = h
 
#size of the map
MAP_WIDTH = w #50
MAP_HEIGHT = h #50
 
LIMIT_FPS = 20  #20 frames-per-second maximum

colors = {
	'dark_wall': libtcod.Color(0, 0, 100),
	'dark_ground': libtcod.Color(50, 50, 150),
	'light_wall': libtcod.Color(130, 110, 50),
	'light_ground': libtcod.Color(200, 180, 50)
}

toggleDisplay = False
 
class Object:
	#this is a generic object: the player, a monster, an item, the stairs...
	#it's always represented by a character on screen.
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
 
	def move(self, dx, dy):
		#move by the given amount, if the destination is not blocked
		if not map[self.x + dx][self.y + dy].blocked:
			self.x += dx
			self.y += dy
 
	def draw(self):
		#set the color and then draw the character that represents this object at its position
		libtcod.console_set_default_foreground(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
 
	def clear(self):
		#erase the character that represents this object
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
 
 

 
def render_all(map):
	#go through all tiles, and set their background color
	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			c = map[x][y].color
			
			
			
			if toggleDisplay == True:
				if c >= 112:
					c = 255
					map[x][y].blocked = False
					map[x][y].block_sight = False
				else:
					c = 0
					map[x][y].blocked = True
					map[x][y].block_sight = True
				wall = map[x][y].block_sight
					
					
					
				if wall:
					libtcod.console_set_char_background(con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
				else:
					libtcod.console_set_char_background(con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
				

			else:
				libtcod.console_set_char_background(con, x, y, libtcod.Color(c, c, c), libtcod.BKGND_SET)
				#libtcod.console_set_char_background(con, x, y, libtcod.Color(c, c, c-100), libtcod.BKGND_SET) ## yellow violet
			
			
			#color = libtcod.Color(c,c,c) #map[x][y].block_sight

			#libtcod.console_set_char_background(con, x, y, color, libtcod.BKGND_SET)
 
	#draw all objects in the list
	for object in objects:
		object.draw()
 
	#blit the contents of "con" to the root console
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

def generate(value):
    values = []
    """
    for x in range(WIDTH):
        for y in range(WIDTH):
            values.append(value(x, y))

    return {
        'width': WIDTH,
        'height': HEIGHT,
        'values': values,
    }
    """

	
 
def handle_keys():
	#key = libtcod.console_check_for_keypress()  #real-time
	key = libtcod.console_wait_for_keypress(True)  #turn-based
	global toggleDisplay
	global map
 
 
	if key.vk == libtcod.KEY_ALT:
		# random value for 
		mySeed = random.random()
		print(mySeed)
		seed = generate_seed(mySeed)
		map =make_map(seed)
		render_all(map)
		libtcod.console_flush()
	
	if key.vk == libtcod.KEY_ENTER:
		#change color : bi to greys
		
		if toggleDisplay == True:
			toggleDisplay = False
		else:
			toggleDisplay = True
		print('toggleDisplay %s' % toggleDisplay)
		render_all(map)
		libtcod.console_flush()
		
		#data = generate(simple_sine)
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		#Alt+Enter: toggle fullscreen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
	elif key.vk == libtcod.KEY_ESCAPE:
		return True  #exit game
 
	#movement keys
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)
 
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
 
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
 
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)
 
 
#############################################
# Initialization & Main Loop
#############################################
 
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
 
#create object representing the player
player = Object(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, '@', libtcod.white)
 
#create an NPC
npc = Object(SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 2, '@', libtcod.yellow)
 
#the list of objects with those two
objects = [npc, player]
 


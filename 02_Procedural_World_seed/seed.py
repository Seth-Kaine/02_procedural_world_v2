import random
VERSION=2

# perlin simplex is more random (perlin classic is more aligned with axes)
from opensimplex import OpenSimplex




def generate_seed(mySeed):
	print(mySeed)
	random.seed(a=mySeed, version=VERSION)
	#random.seed( mySeed ) # accept txt
	rand01 = random.random() 
	"""
	print ("rand01 - ", rand01 )
	print ("rand01 - ", rand01 )
	print ("seed 01  - ", random.random() )
	
	print ("seed 02 - ", random.random() )
	print ("seed 03 - ", random.random() )
	"""
	r = int(rand01*10000)
	print(r)
	tmp = OpenSimplex(r) # don't accept txt
	#print(tmp)
	return tmp
	"""
	#if you want to use the same random number once again, then use the same seed value
	print ("Random number with seed : %s" % mySeed)
	random.seed(a=mySeed, version=VERSION)
	print ("first - (VERSION %s) %s  " % (VERSION,random.randint(25,50)))  #will generate a random number
	#will generate a same random number as previous
	random.seed( mySeed )
	print ("Second - ", random.randint(25,50))
	#will generate a same random number as previous
	random.seed( mySeed )
	print ("Third - ", random.randint(25,50))
	random.seed( mySeed )
	print ("Fourht - ", random.random() )
	"""

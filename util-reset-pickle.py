#!/usr/bin/python3
# Andrew Kerr
# 1/28/2020

'''Simply resets the pickle file back to default values.'''

import pickle

games = {1 : ['FPS','Halo3','Bungee','Microsoft','xbox360','2007','10','either','30.00','Yes','1/25/2008','This game blows chunks'] }

datafile = open("game_lib.pickle","wb")
pickle.dump(games,datafile)
datafile.close()
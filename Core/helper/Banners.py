import sys
import time
import os
import logging

logger = logging.getLogger(__name__)

def PlanetBanner():
	try:
		os.system("clear")
		
		Planet = ("""
                                                     ___
                                                  ,o88888
                                               ,o8888888'
                         ,:o:o:oooo.        ,8O88Pd8888"
                     ,.::.::o:ooooOoOoO. ,oO8O8Pd888'"
                   , ..:.::o:ooOoOoOO8O8OOo.8OOPd8O8O"
                  , ..:.::o:ooOoOOOO8OOOOo.FdO8O8"
                 , ..:.::o:ooOoOO8O888O8O,COCOO"
                , . ..:.::o:ooOoOOOO8OOOOCOCO"
                 . ..:.::o:ooOoOoOO8O8OCCCC"o
                    . ..:.::o:ooooOoCoCCC"o:o
                    . ..:.::o:o:,cooooCo"oo:o:
                 `   . . ..:.:cocoooo"'o:o:::'
                 .`   . ..::ccccoc"'o:o:o:::'
                :.:.    ,c:cccc"':.:.:.:.:.'
              ..:.:"'`::::c:"'..:.:.:.:.:.'
            ...:.'.:.::::"'    . . . . .'
           .. . ....:."' `   .  . . ''
         . . . ...."'
         .. . ."'     
        .
		""")
		for line in Planet:                   
			print(line, end='')    
			sys.stdout.flush()  
			time.sleep(0.001)          
	except Exception as e:
		logger.error(f"Error displaying PlanetBanner: {e}")
		print(f"[!] Error: Could not display banner - {e}")

import os
import sys
import logging

try:
    from colorama import Fore
except ImportError as e:
    logging.error(f"Failed to import colorama: {e}")
    print(f"[!] Error: colorama module not found - {e}")
    sys.exit(1)

logger = logging.getLogger(__name__)

red = "\033[1;31;40m"
green = "\033[1;32;40m"
white = "\033[1;37;40m"
blue = "\033[1;34;40m"
yellow = Fore.CYAN
purple = Fore.MAGENTA


start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def numbering(num):
  return green + "[" + white + str(num) + green + "]"

def CurrentDir():
	try:
		path = os.getcwd()
		print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path)
	except Exception as e:
		logger.error(f"Failed to get current directory: {e}")
		print(f"[!] Error: Could not determine current directory - {e}")

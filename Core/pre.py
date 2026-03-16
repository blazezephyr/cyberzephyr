import os
import random
import logging
import sys

try:
    from rgbprint import gradient_print
except ImportError as e:
    logging.error(f"Failed to import rgbprint: {e}")
    print(f"[!] Warning: rgbprint module not found - {e}")
    print("[*] Using fallback banner display...")
    gradient_print = None

try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    try:
        os.system("pip install colorama")
        from colorama import Fore, Style
    except Exception as e:
        logging.error(f"Failed to install colorama: {e}")
        print(f"[!] Error: Could not install colorama - {e}")
        sys.exit(1)
except ImportError as e:
    logging.error(f"Failed to import colorama: {e}")
    print(f"[!] Error: colorama module not found - {e}")
    sys.exit(1)

try:
    from urllib.request import urlopen
except ImportError as e:
    logging.error(f"Failed to import urlopen: {e}")
    print(f"[!] Error: urllib module not available - {e}")
    sys.exit(1)

try:
    from Core.helper.color import green, white, blue, start, alert , yellow , purple
except ImportError as e:
    logging.error(f"Failed to import helper color module: {e}")
    print(f"[!] Error: Helper color module not found - {e}")
    sys.exit(1)

logger = logging.getLogger(__name__)

green = yellow
red = purple
white = purple

Version = "2.2"
yellow = ("\033[1;33;40m")

banner = f"""
   root@darknet:~# access system
root@darknet:~# initializing protocol...

██████╗ ██╗      █████╗ ███████╗███████╗
██╔══██╗██║     ██╔══██╗╚══███╔╝██╔════╝
                     B L A Z E   Z E P H Y R

	===========================================================
			Blaze Zephyr - Phishing Tool
	===========================================================
"""


def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host, timeout=10)
        return True
    except Exception as e:
        logger.error(f"Connection check failed for {host}: {e}")
        return False


all_col = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.LIGHTCYAN_EX,
           Style.BRIGHT + Fore.LIGHTBLUE_EX, Style.BRIGHT + Fore.LIGHTCYAN_EX, Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
           Style.BRIGHT + Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)


def menu():
    try:
        if gradient_print is not None:
            gradient_print(banner, start_color='yellow', end_color='magenta')
        else:
            print(banner)
        print(alert + " More Versions Will Come Soon Stay Updated, Follow My Github\n")
        print(white + "options:")
        print(
            green + "[" + white + "1" + green + "]" + white + " Instagram" + green + "\t\t\t[" + white + "12" + green + "]" + white + " Paypal")
        print(
            green + "[" + white + "2" + green + "]" + white + " Facebook" + green + "\t\t\t[" + white + "13" + green + "]" + white + " Discord")
        print(
            green + "[" + white + "3" + green + "]" + white + " Gmail" + green + "\t\t\t[" + white + "14" + green + "]" + white + " Spotify")
        print(
            green + "[" + white + "4" + green + "]" + white + " Gmail (simple)" + green + "\t\t[" + white + "15" + green + "]" + white + " Blockchain")
        print(
            green + "[" + white + "5" + green + "]" + white + " Twitter" + green + "\t\t\t[" + white + "16" + green + "]" + white + " RiotGames")
        print(
            green + "[" + white + "6" + green + "]" + white + " Snapchat" + green + "\t\t\t[" + white + "17" + green + "]" + white + " Rockstar")
        print(
            green + "[" + white + "7" + green + "]" + white + " Snapchat (simple)" + green + "\t\t[" + white + "18" + green + "]" + white + " AskFM")
        print(
            green + "[" + white + "8" + green + "]" + white + " Steam" + green + "\t\t\t[" + white + "19" + green + "]" + white + " 000Webhost")
        print(green + "[" + white + "9" + green + "]" + white + " Dropbox" + green)
        print(
            green + "[" + white + "10" + green + "]" + white + " Linkedin" + green + "\t\t\t[" + white + "21" + green + "]" + white + " Gamehag")
        print(
            green + "[" + white + "11" + green + "]" + white + " Playstation" + green + "\t        [" + white + "22" + green + "]" + white + " Mega")
        print(green + "-----------------------------------------------------------------------")
        print(green + "[" + white + "00" + green + "]" + red + " EXIT")
    except Exception as e:
        logger.error(f"Error displaying menu: {e}")
        print(f"[!] Error: Could not display menu - {e}")


def Welcome():
    try:
        os.system("clear")
    except Exception as e:
        logger.error(f"Failed to clear screen in Welcome: {e}")
        print(f"[!] Warning: Could not clear screen - {e}")

menu()

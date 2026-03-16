import platform
import sys
import os
import logging
from sys import version_info

if version_info < (3, 0, 0):
    print('[!] Please use Python 3. $ python3 CyberPhish.py')
    sys.exit()

from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import Blockchain
from Core.eletter import Spotify
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import Mega
from Core.eletter import RiotGames
from Core.eletter import Steam

from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.eletter import Playstation
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat
from Core.pre import *
from Core.helper.RedirectBypass import *
from rgbprint import gradient_print
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.CYAN

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='blaze_zephyr.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

try:
    os.system("clear")
except Exception as e:
    logger.error(f"Failed to clear screen: {e}")
    print(f"[!] Warning: Could not clear screen - {e}")


def CurrentDir():
    try:
        path = os.getcwd()
        print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')
    except Exception as e:
        logger.error(f"Failed to get current directory: {e}")
        print(f"[!] Error: Could not determine current directory - {e}")
        sys.exit(1)


no = ["n", "no"]
cont = ""
while cont not in no:
    def mainMenu():
        os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
        menu()

        print(green)

        CurrentDir()

        try:
            mailPick = int(input(green + "root@BlazeZephyr ~> " + white))
        except ValueError:
            logger.error("Invalid input - not a number")
            print("\n[!] Error: Please enter a valid number")
            input("Press Enter to continue...")
            return False
        except KeyboardInterrupt:
            logger.info("User interrupted input")
            print("\nExiting tool....")
            Welcome()
            return "exit"
        except EOFError:
            logger.error("EOF encountered during input")
            print("\n[!] Error: Input interrupted")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error during input: {e}")
            print(f"\n[!] Error: {e}")
            sys.exit(1)

        try:

            if mailPick == 1:
                Instagram()

            elif mailPick == 2:
                Facebook()

            elif mailPick == 3:
                Gmail()

            elif mailPick == 4:
                GmailActivity()

            elif mailPick == 5:
                Twitter()

            elif mailPick == 6:
                Snapchat()

            elif mailPick == 7:
                SnapchatSimple()

            elif mailPick == 8:
                Steam()

            elif mailPick == 9:
                Dropbox()

            elif mailPick == 10:
                Linkedin()

            elif mailPick == 11:
                Playstation()

            elif mailPick == 12:
                Paypal1()

            elif mailPick == 13:
                Discord()

            elif mailPick == 14:
                Spotify()

            elif mailPick == 15:
                Blockchain()

            elif mailPick == 16:
                RiotGames()

            elif mailPick == 17:
                Rockstar()

            elif mailPick == 18:
                AskFM()

            elif mailPick == 19:
                Webhost000()

            elif mailPick == 20:
                Dreamteam()

            elif mailPick == 22:
                Mega()

            elif mailPick == 69:
                RedirectionMain()

            elif mailPick == 00:
                os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
                print("- Hope I See You Soon")
                print("- Happy Phishing")
                return "exit"

            else:
                print("\n- Something Went Wrong There Partner")
                return False

        except ValueError as e:
            logger.error(f"Value error in menu selection: {e}")
            print("\n[!] Error: Invalid selection - Please enter a valid number")
            input("Press Enter to continue...")
            return False
        except KeyboardInterrupt:
            logger.info("User interrupted with Ctrl+C")
            print("\nExiting tool....")
            Welcome()
            return "exit"
        except EOFError:
            logger.error("EOF encountered during execution")
            print("\n[!] Error: Input interrupted unexpectedly")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error in main menu: {e}")
            print(f"\n[!] Error: Something went wrong - {e}")
            input("Press Enter to continue...")
            return False

    result = mainMenu()
    if result == "exit":
        break
    if result is False:
        continue

    try:
        cont = input(red + "Do you want to continue? [y/n] :")
        if cont.lower() in ["y", "yes"]:
            os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
            menu()
        elif cont.lower() in ["n", "no"]:
            print("\nExiting Blaze Zephyr...")
            sys.exit(0)
        else:
            print("\n[!] Invalid input. Exiting...")
            sys.exit(0)
    except KeyboardInterrupt:
        logger.info("User interrupted continue prompt")
        print("\nExiting Blaze Zephyr...")
        sys.exit(0)
    except EOFError:
        logger.error("EOF encountered in continue prompt")
        print("\n[!] Error: Input interrupted. Exiting...")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error in continue prompt: {e}")
        print(f"\n[!] Error: {e}. Exiting...")
        sys.exit(1)

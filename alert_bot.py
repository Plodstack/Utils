import telegram
import sys
import argparse
import time
import netifaces as ni
import colorama
from pathlib import Path
from colorama import Fore

msg_content = None

#time.sleep(30)
# Grab the arguments from the command line
parser = argparse.ArgumentParser(description='A chatbot alerter, text field will be processed then file appended to the text')
parser.add_argument("-t", metavar ="\"Your message\"", help="Text",type=str)
parser.add_argument("-f", metavar ="\"/mypath/mytext.txt\"",help="Location of text file for message body",type=Path)
args = parser.parse_args()
text_from_argument = args.t
file_from_argument = args.f
#print(text_from_argument)

#logfile = open("/home/pi/logging.log", "a")

# if there is a text specified then use that
if text_from_argument is not None:
	msg_content = text_from_argument

# if there is a file argument specified then grab the contents append to the text if specified
if file_from_argument is not None:
	filelocation  = open(file_from_argument, "r")
	msg_content = str(text_from_argument) + "\n" + (filelocation.read())

if msg_content is None:
	print (Fore.RED + "Error: You must specify a file or a text to send. See --help")
	sys.exit()


ni.ifaddresses('wlan0')
retry = 0
while True:
	try:
		ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
	except Exception:
		retry = retry + 1
#		logfile.write (str(retry))
#		logfile.write ("Interface is not up.\n")
		time.sleep(5)
		if retry >= 5:
#			logfile.write ("It took too long for the interface to come up")
#			logfile.close()
			sys.exit()
	else:
#		logfile.write ("Interface is up.\n")
#		logfile.write (ip)
		break


if msg_content is not None:
	bot = telegram.Bot("")
	def sendTelegram(msg_content):
	   bot.sendMessage(chat_id='', text=msg_content, disable_web_page_preview=True)
	   return None
	sendTelegram(msg_content)

#logfile.close()
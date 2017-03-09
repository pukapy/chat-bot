from time import strftime
from engine import Bot
import requests
import random
import sys

tiktak = strftime("%y-%m-%d %H-%M-%S")
tiktaktoe = strftime("%y-%m-%d")
lucky = Bot()
lucky.login()
lastPrinted = []
logs = open('logs/Logs {}.txt'.format(tiktaktoe), 'a')
while True:
	msg = lucky.goChat()
	lastMsg = lucky.get_last_message(msg)
	if lastMsg != lastPrinted:
		lastPrinted = lastMsg
		hany = lastMsg
		print "{} : {}".format(hany[0], hany[1])
		logs.write("{} {} : {} \n".format(tiktak, hany[0], hany[1]))




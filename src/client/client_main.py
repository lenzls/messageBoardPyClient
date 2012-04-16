# -*- coding: utf-8 -*-

#-------------------------------------------------------------------
#| see posted messages and webinterface on http://mb.simon-lenz.de |
#-------------------------------------------------------------------

import socket
import time
import json

SERVERIP = "www.simon-lenz.de"
SERVERPORT = 52222

if __name__ == "__main__":
	nick = raw_input("Nickname:")

	while (True):
		msg = raw_input("Nachricht (\"ende\" zum Beenden):")
		if msg == "ende":
			break

		#--nicht unbedingt nötig--
		#nick_uni = nick.decode(sys.stdin.encoding)
		#msg_uni = msg.decode(sys.stdin.encoding)
		#nick_utf8 = nick_uni.encode("utf-8")
		#msg_utf8 = msg_uni.encode("utf-8")
		#-------------------------

		data = {"nickname": nick, #nick_utf8,
				"senderIPPORT": 0,
				"sendtime": time.time(),
				"recvtime": 0,
				"message": msg} #msg_utf8}

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((SERVERIP, SERVERPORT))
		s.send(json.JSONEncoder().encode(data))
		s.close()

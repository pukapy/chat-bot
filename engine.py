import requests, lxml.html
import re
import sys
import json

class Bot:
    def __init__(self):
        self.login_link = "https://rstforums.com/forum/login/"
        self.chat_link = "https://rstforums.com/forum/chat/"
        self.s = requests.session()
        self.key = ""   # acces_key
        self.user = ""  # user
        self.link = "https://server10.ips-chat-service.com/get.php?room=5764&user=" + str(self.user) + "&access_key=" + str(self.key)
        self.send_link = "https://server10.ips-chat-service.com/post.php?room=5764&user=" + str(self.user) + "&access_key=" + str(self.key)

    def login(self):
        login = self.s.get(self.login_link)
        login_html = lxml.html.fromstring(login.text)
        hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
        form = {
            x.attrib["name"]: x.attrib["value"] for x in hidden_inputs
            }
        x = form['auth'] = ""       # user
        form['password'] = ""       # parola
        response = self.s.post(self.login_link, data=form)
        if x in response.text:
            print "WORKING"
        else:
            print "not working" 
            sys.exit("Failed to log-in.")   

    def goChat(self):
        pac = self.s.get(self.link)
        return pac.content

    def get_last_message(self, msg):
        split = msg.split("~~||~~")
        bList = []
        try:
            for x in split:
                bList.append(x.split(','))
            l = [
                bList[-2][2].replace("__N__", "\n").replace("__C__", ",").replace("__E__", "=").replace("__PS__", "+").replace("__A__", "&").replace("__P__", "%").replace("&#039", "'").replace("&amp;gt;", ">").replace("&amp;lt;", "<").replace("&quot", '"'),
                bList[-2][3].replace("__N__", "\n").replace("__C__", ",").replace("__E__", "=").replace("__PS__", "+").replace("__A__", "&").replace("__P__", "%").replace("&#039", "'").replace("&amp;gt;", ">").replace("&amp;lt;", "<").replace("&quot", '"')
            ]
            return l
        except IndexError:
            pass

    def send(self, msg):
        self.s.post(self.send_link, data = {'message': msg})

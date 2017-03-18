#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


def straightBet(s):
	url = "http://888east.com/wager/CreateSports.aspx?WT=0"
	user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
	r = s.get(url,headers=user, timeout=5, cookies=s.cookies)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")

	games = {}
	for eachGame in soup.find_all("table",{"cellpadding":"5"}):
		for game in eachGame.find_all("tr"):
			gameID = game.find_all("input",{"type":"checkbox"})
			gameName = game.find_all("span",{"class":"link"})
			if gameID:
				if "checkbox" in str(gameID[0]):
					print(gameName[0].text)
					games[gameName[0].text] = gameID[0].get('name')

	chosenGame = input("Which game? ")

	

def getdata(s):
	mainURL = "http://888east.com/wager/Message.aspx"
	user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
	r = s.get(mainURL,headers=user, timeout=5, cookies=s.cookies)

	data = r.text
	soup = BeautifulSoup(data,"html.parser")

	tag = "ctl00_ctl02_lbl"
	for items in soup.find_all("div",{"style":"padding-left:113px; padding-top:15px;"}):
		if "ctl00_ctl02_lbl" in str(items):
			infoName = str(items.find('span').get('id')).replace('ctl00_ctl02_lbl','')
			infoValue = items.find('span').text
			print(infoName + " : " + infoValue)

def login(s,data):
	# URL's 
	loginURL = "http://888east.com/default.aspx?"
	user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
					"Accept": "*/*",
    			"Accept-Encoding": "gzip,deflate,sdch",
    			"Accept-Language": "en-US,en;q=0.8"
}


	# Get data, doesnt change now, but if it does...
	soup = BeautifulSoup(data,"html.parser")
	__VIEWSTATE = str(soup.find(id="__VIEWSTATE").get('value')).replace('/','%2F')
	__VIEWSTATEGENERATOR = str(soup.find(id="__VIEWSTATEGENERATOR").get('value')).replace('/','%2F')
	__EVENTVALIDATION = str(soup.find(id="__EVENTVALIDATION").get('value')).replace('/','%2F')


	logIn = input("username: ")
	password = input("password: ")
	print("\n")


	logInData = [
		"__EVENTTARGET"+"="+"",
		"__EVENTARGUMENT"+"="+"",
		"__VIEWSTATE"+"="+__VIEWSTATE,
		"__VIEWSTATEGENERATOR"+"="+__VIEWSTATEGENERATOR,
		"__EVENTVALIDATION"+"="+__EVENTVALIDATION,
		"ctl00%24MainContent%24ctlLogin%24_UserName"+"="+logIn,
		"ctl00%24MainContent%24ctlLogin%24_Password"+"="+password,
		"ctl00%24MainContent%24ctlLogin%24BtnSubmit.x"+"="+"35",
		"ctl00%24MainContent%24ctlLogin%24BtnSubmit.y"+"="+"16",
		"ctl00%24MainContent%24ctlLogin%24_IdBook"+"="+"",
		"ctl00%24MainContent%24ctlLogin%24Redir"+"="+""
		]

	for items in logInData:
		loginURL += items + "&"
	loginURL = loginURL[:-1]

	r = s.get(loginURL,headers=user, timeout=5, cookies=s.cookies)

def loadCookies(s):
	user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"}
	r = s.get("http://888east.com/",headers=user, timeout=5, cookies=s.cookies)
	return r.text

def main():
	s = requests.Session()

	# Might need if site checks cookies
	data = loadCookies(s)

	# Log in...
	login(s,data)

	# Get data or whatever
	getdata(s)

	input("Find games? ")
	# straight bet
	straightBet(s)

if __name__ == '__main__':
	main()

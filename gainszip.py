import requests
from bs4 import BeautifulSoup
from time import sleep



url = "https://affi.cryptoplanets.org/btcgains/index.php"
urlclaim = "https://affi.cryptoplanets.org/btcgains/ajax.php"

UA = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; vivo Y31L Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36"

}

data = {
  "PHPSESSID": "htsep29sgknl5m2vnpg1uj7011"

}

claim1 = {
  "confirm_exploaration_point_claim": "1"
}
claim2 = {
  "confirm_exploaration_point_claim": "2"
}
claim3 = {
  "confirm_exploaration_point_claim": "3"
}
claim4 = {
  "confirm_exploaration_point_claim": "4"
}
claim5 = {
  "confirm_exploaration_point_claim": "5"
}

reset1 = {
  "reset_contest_button": "1"
}
reset2 = {
  "reset_contest_button": "2"
}
reset3 = {
  "reset_contest_button": "3"
}
reset4 = {
  "reset_contest_button": "4"
}
reset5 = {
  "reset_contest_button": "5"
}

c = requests.Session()

def login():
    r = c.post(url, cookies=data, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    ball = soup.find_all('div', class_="widget-int num-count")
    for ballance in ball:
        print ("Login")
        sleep(2)
        print ("Your Ballance :", ballance.text, "gains")

def button1():
   c.post(urlclaim, cookies=data, headers=UA, data=reset1)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim1)
   print ("success :", r.text, "point")
def button2():
   c.post(urlclaim, cookies=data, headers=UA, data=reset2)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim2)
   print ("success :", r.text, "point")
def button3():
   c.post(urlclaim, cookies=data, headers=UA, data=reset3)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim3)
   print ("success :", r.text, "point")
def button4():
   c.post(urlclaim, cookies=data, headers=UA, data=reset4)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim4)
   print ("success :", r.text, "point")
def button5():
   c.post(urlclaim, cookies=data, headers=UA, data=reset5)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim5)
   print ("success :", r.text, "point")

def gains():
    login()
    while True:
          button1()
          sleep(60)
          button2()
          sleep(60)
          button3()
          sleep(60)
          button4()
          sleep(60)
          button5()
          sleep(60)

gains()

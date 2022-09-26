#!/usr/bin/env python3
import cgi, cgitb, secret,os
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie

#set up cgi form
form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

#check if correct login info provided to cgi form
form_ok = username == secret.username and password == secret.password

#setup cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

#check if correct login info provided to cookie
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

#set usernmae and password to cookie
if cookie_ok:
    username = cookie_username
    password = cookie_password

#print it to html
print("Content-type: text/html")
if form_ok:
   # set cookie iff login info is correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

#load login page, print user form info
if username == None and password == None:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username,password))
else:
    print(after_login_incorrect())
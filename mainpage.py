#!/usr/bin/python

import Cookie,os

import cgitb,hashlib,cgi
cgitb.enable()

form=cgi.FieldStorage()

f = open('data/users.txt', 'r')
text = f.read().split('\n') 
f.close()

head = '''<!DOCTYPE html>
<html>
 <head>
  <title>Login page</title>
 <style>
 body {
   background-color: #D08BE5;
 }
  h1 { 
    color: Yellow;
    text-align: left;
    font-family: "Monotype Corsiva";
    font-size: 60px;
  }
  h2 {
    color: #FFF763;
    text-align: center;
    font-family: "Verdana";
    font-size: 35px;
  }
  h3 {
    color: Blue;
    text-align: center;
    font-family: "Verdana";
    font-size: 20px;
  }
  p  {
    color: Purple;
    text-align: left;
    font-family: "Times New Roman";
    font-size: 20px;
  }
  tr:hover {
    background-color: #F5F5F5
  }
  td {
    color: black;
    text-align: center;
    font-family: "Nyala";
    font-size: 20px;
  }
  table.center {
    margin-left:auto;
    margin-right:auto;
  }
  img.displayed {
    display: blcok;
    margin-left: auto;
    margin-right: auto;
  }
  .resize {
    width: 200px;
    height: auto;
  }
 </style>
 </head>
 <body>
   '''
def makePage(): #sets up code to determine the factions of new users via test
    if "faction" not in form:
        ans = '<a href="test1.py">Take the test!</a><br>'
    return ans

            

body = "<h1> WELCOME"  
foot = '''</body>
</html>
'''

def authenticate(u,ID,IP):
    loggedIn = open('data/loggedin.txt','r').read().split('\n')
    loggedIn = [each.split(',') for each in loggedIn]
    loggedIn.remove([''])
    for a in loggedIn:
        if a[0] == username:
            return a[1]==str(ID) and a[2]==IP
    return False

abnegation=[]
amity=[]
candor=[]
dauntless=[]
erudite=[["A coin is weighted so that the probability of heads is 2/3. What is the probability of getting exactly two heads in five tosses of the coin?, 40/243"],["The sum of the first five terms of an arithemtic series is 70, while the sum of the first ten terms of the same series is 210. What is the first term?, 42/5"]]
#Question pool: Abnegation: 0 Amity: 0 Candor: 0 Dauntless: 0 Erudite: 2

#def test2():


    


if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)
    ##print all the data in the cookie
    #body+= "<h1>cookie data</h1>"
    #for each in c:
    #    body += each+":"+str(c[each].value)+"<br>"
    if 'username' in c and 'ID' in c:
        username = c['username'].value
        ID = c['ID'].value
        IP = os.environ['REMOTE_ADDR']
        
        ##print all the users logged in
        #body += "<h1>userstuff</h1>"
        #body += str(loggedIn)
        #body += "<br>"
        if authenticate(username,ID,IP):
            body+=makePage()
        else:
            body+="Failed to Authenticate cookie<br>\n"
            body+= 'Go Login <a href="login.py">here</a><br>'
    else:
        body+= "Your information expired<br>\n"
        body+= 'Go Login <a href="login.py">here</a><br>'
else:
    body+= 'You seem new<br>\n'
    body+='Go Login <a href="login.py">here</a><br>'
    body+='Or create an account <a href="createaccount.py">here</a>'

#body = "<h1> WELCOME" + test
#foot = '''</body>
#</html>
#'''


print 'content-type: text/html'
print ''
print head
print body
print foot

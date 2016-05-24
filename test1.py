#!/usr/bin/python
import cgitb,hashlib,cgi
cgitb.enable()

form=cgi.FieldStorage()

test1=[["question1, ans1, ans2"], ["question2, ans1, ans2"], ["question3, ans1, ans2"]]
def test():
        y = 0
        ans = "<h3> From Abnegation: " + form.getvalue("username").capitalize() + "</h3>"
        ans += "<form method = 'GET' action = 'mainpage.py'>"
        for each in test1: 
            y += 1
            each = ''.join(each)
#            ans += each
#	    for item in each:
            each = each.split(",")
#            ans += each[1] 
            ans += each[0] + "<br>" + each[1] + "<input type='radio' name='question" + str(y) + "' value='" + str(each[1]) + "' checked >"
            ans += each[2] + "<input type='radio' name='question" + str(y) + "' value='" + str(each[2]) + "'>"
	    ans += "<br> <br>"
	ans += 	'''<input type="submit" name="submit" value="I'm done.">'''
        return ans

print 'content-type: text/html'
print test()

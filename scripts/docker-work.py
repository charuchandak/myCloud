#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print

name=cgi.FormContent()['conname'][0]
work=cgi.FormContent()['work'][0]

if work == 'shell':
#check that container is running or not
	print "live shell"
	print "<form action='docker-shell.py'>"
	print "<input type='hidden' name='cname' value='{}' />".format(name)
	print "<textarea cols='50' rows='10' name='code'>"
	print "</textarea>"
	print "<input type='submit'>"
	print "</form>"
	print "<a href='docker-manage.py'>go back</a>"	


elif work == 'server':
	print "setting up your server"
	print "processing..."
	print "will complete soon" 
	print "<a href='docker-manage.py'>go back</a>"  


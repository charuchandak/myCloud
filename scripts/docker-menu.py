#!/usr/bin/python2
import commands
import cgi

print "Content-Type: text/html"
print

name=cgi.FormContent()['cname'][0]
print "<pre>"
print "!!!!!! please check against the container name !!!!!!"
print 
print "Docker Menu"
print "<form action='docker-work.py'>"
print "<input type='checkbox' name='cname' value='{0}' />{0}".format(name)
print "<input type='radio' name='work' value='status' />status of container"
print "<input type='radio' name='work' value='server' />setup server and commit your image"
print "<input type='radio' name='work' value='stop' />stop your container"
print "<input type='radio' name='work' value='shell' />Get a live shell"
print "<input type='submit' />"
print "<a href='docker-launch.py'>go back</a>"

print "</form>"
print "</pre>"


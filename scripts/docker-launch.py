#!/usr/bin/python2
import cgi
import commands
print "content-type: text/html"
print

a= cgi.FormContent()
l=len(a)
#print a

image_type=[]
container_name=[]
i=1
print "<center>"
print "<pre>"
print "<h2>your containers have been launched</h2><br />"
while i<=(l/2):
	x="c=cgi.FormContent()['con{}'][0]".format(i)
	exec(x)
	container_name.append(c)
	
	y="d=cgi.FormContent()['image{}'][0]".format(i)
        exec(y)
	image_type.append(d)
#print container_name[0]
#print image_type[0]
	commands.getstatusoutput("sudo docker run -dit --name {0} {1}".format(container_name[i-1],image_type[i-1]))
	
	ipstatus=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(container_name[i-1]))
	#print "<br />"
	print ipstatus+ " is the IP Address of the container - {0} ".format(container_name[i-1])
	print
	i+=1
print "<a href='docker-manage.py'><h3>click here to manage your container</h3></a>"
print "</pre>"
print "</center>"


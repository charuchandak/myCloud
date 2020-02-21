#!/usr/bin/python2
import cgi
import commands
print "content-type: text/html"
print

print """
<script>
function rm(mycname)
{
document.location='docker_remove.py?x=' + mycname;
}

function stop(mycname)
{
document.location='docker_stop.py?x=' + mycname;
}

function start(mycname)
{
document.location='docker_start.py?x=' + mycname;
}

</script>
"""



print "<center>"
print "<pre>"
print
print "<h1>--- LIST OF LAUNCHED CONTAINER ---</h1>"
a= commands.getoutput("sudo docker ps -a")
b = a.splitlines()
i=0
l=len(b)
c=[]
d=[]

print "<table border='3'>"
while i < l:
        t=" ".join(b[i].split())
        c.append(t)
        d.append(c[i].split(" "))
        i+=1
print "<h2>"
print "<tr><th>Container_NAME </th><th>Image_NAME:version</th><th>IP_Address</th><th>STATUS</th><th>START</th><th>STOP</th><th>REMOVE</th></tr>"
i=1
l=len(d)
while i< l:
        ipstatus=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(d[i][-1]))
	status = commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(d[i][-1]))
	print "<tr><th>"+ d[i][-1] + "</th><th>" + d[i][1] +"</th><th>"+ ipstatus +"</th><th>"+ status +"</th><td> <input value='" + d[i][-1]    +  "' type='button' onclick=start(this.value)  />   </td><td>  <input value='" + d[i][-1]    +  "' type='button' onclick=stop(this.value)  /> </td><td>  <input value='" + d[i][-1]  +  "' type='button' onclick=rm(this.value)  /> </td></tr>"
        i+=1
print "</h2>"
print "</table>"
print "<hr />"
print "</pre>"
print "<form action='docker-work.py'>"
print "Enter container name<input type='text' name='conname'>"
print "<input type='radio' name='work' value='shell'>Launch a live Shell"
print "<input type='radio' name='work' value='shell'>deploy server and commit image"
print "<input type='submit'>"

print "</center>"

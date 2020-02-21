#!/usr/bin/python2
import commands
import cgi
import re
print "Content-Type: text/html"
print


print """
<html>
<head>

<style type="text/css">
/* BodyBackgound*/

body {

  background: #A9A9A9 ;

}

.mainframe{
	position: relative;
	background: #FFFFFF;	
	box-shadow: 0 0 20px 0 rgba(0, 0, 0, 20), 0 5px 5px 0 rgba(0, 	0, 0, 0.24);
	width:1024px;
	margin:auto;

}

/*body Background END */

/*Header START*/
.Header{
	width:1024px;
	height:150px;
	margin:auto;
	background: #FFFFFF;
}
/*Header END */

/*menu*/
.menu{
	width:1024px;
	height:50px;
	margin:auto;
	overflow: hidden;
	font-family: "Roboto", sans-serif;
	background-color: #292C2F;
	padding:0;
}

.menu a {
	float: left;
	font-size: 16px;
	color: white;
	text-align: center;
	padding: 14px 16px;
	text-decoration: none;
}

.dropdown {
	float: left;
	overflow: hidden;
}

.dropdown .dropbtn {
	font-size: 16px;    
	border: none;
	outline: none;
	color: white;
	padding: 14px 16px;
	background-color: inherit;
}

.menu a:hover, .menu .dropdown:hover .dropbtn {
	background-color: #4CAF50;
	color:#000000;
}

.dropdown-content {
	display: none;
	position: absolute;
	background-color: white;
	min-width: 160px;
	box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	z-index: 1;
}

.dropdown-content a {
	float: none;
	color: black;
	padding: 12px 16px;
	text-decoration: none;
	display: block;
	text-align: left;
}

.dropdown-content a:hover {
	background-color: #ddd;
	font-color:#000000;
}

.dropdown:hover .dropdown-content {
	display: block;
}		
	
/*menu end */

/* content part START*/
	/* text part START*/

.heading{
	text-align:center;
}

/* text part END*/
/*Form START*/
.form {
  position: relative;
  background: #FFFFFF;
  max-width: 360px;
  padding: 45px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  margin:auto;
}

.form input {
  font-family: "Roboto", sans-serif;
  outline: 0;
  background: #f2f2f2;
  width: 100%;
  border: 0;
  margin: 0 0 15px;
  padding: 15px;
  box-sizing: border-box;
  font-size: 14px;
}
.form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4CAF50;
  width: 100%;
  margin: 0 0 15px;
  
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
}
.form button:hover,.form button:active,.form button:focus {
  background: #43A047;
}

.checkbox{
	  position: relative;
	  background: #FFFFFF;
	  max-width: 360px;
	  padding: 45px;
	  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
	  margin:auto;
}


}

.radio{
  	  box-sizing:border-box;
	  position: relative;
	  background: #FFFFFF;
	  max-width: 360px;
	  padding: 45px;
	  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
	  margin:auto;

}

/* Docker Form */
.dokcer-form {
  position: relative;
  background: #FFFFFF;
  max-width: 360px;
  padding: 45px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  margin:auto;
}
.docker-form button {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #4CAF50;
  width: 350px;
  margin: auto;
  
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 14px;
}
.docker-form button:hover,.docker-form button:active,.docker-form button:focus {
  background: #43A047;
}

/* Docker Form END*/
/*From END*/

/* content part END

/* Footer */

footer{
	background-color:#292C2F;
	text-align:center;
	
}
p.our-motto{
	padding: 15px;
	color:#000000;
	margin:auto;	
}


.footer_links{
	text-align:center;
	font-weight: bold;
	color: #ffffff;
	margin: 0 0 10px;
	padding: 0;
}

.footer_links a{
	color:#FFFFFF;
	text-decoration: none;
}

.footer_links a:hover{
	color:#4CAF50;
	text-decoration: none;
}

.footer_links a:focus{
	color:#4CAF50;
	text-decoration: none;
}

p.Team-name{
	
	padding:10px;
	color:#000000;
	margin:auto;
}



/* Footer End*/ 

/* Ids */
#table{  
  position: relative;
  background: #FFFFFF;
  max-width: 360px;
  padding: 45px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
  margin:auto;
 
}




/* Ids END*/



</style>

<title>CAAS</title>

</head>

<!-- Body START -->

<body>

<div class="mainframe">
	
		<div class="Header">
			<img src="https://github.com/charuchandak/myCloud/tree/master/images/header.jpg" />
    	</div>
		
        <!-- menu START -->
            
   	 	<div class="menu">

        

                <!-- Home button -->

                 <a href="https://github.com/charuchandak/myCloud/tree/master/index.html" >Home</a>

                <!-- Home button end -->

                

                <!-- News button -->

                 <a href="#news">News</a>

         		<!-- News button end -->	

              	

                <!-- SAAS button -->

		    	 <div class="dropdown">

                    <button class="dropbtn">SAAS</button>

                    	<div class="dropdown-content">

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">Firefox</a>

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">VLC</a>

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">MediaPlayer</a>

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">Outlook</a>

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">Adobe</a>

                          <a href="https://github.com/charuchandak/myCloud/tree/master/saas.html">C panel</a>

                    </div>

                 </div> 

				<!-- SAAS button end-->

                

                <!-- STAAS button -->

		  		 <div class="dropdown">

		  			  <button class="dropbtn">STAAS</button>

					      <div class="dropdown-content">

                              <a href="https://github.com/charuchandak/myCloud/tree/master/nfs.html">Object Storage</a>

                              <a href="https://github.com/charuchandak/myCloud/tree/master/blockstorages.html">Block Storage</a>

					</div>

		 	 	 </div>

                <!-- STAAS button end--> 

                

		<!-- CAAS button -->

                 <div class="dropdown">

			

			 <button class="dropbtn">CAAS</button>
				 <div class="dropdown-content">

                             		 <a href="https://github.com/charuchandak/myCloud/tree/master/scripts/caashome.py">Docker</a>


					</div>	

				

		 </div>

                 <!-- CAAS button end-->

                 

                 <!-- IAAS button -->

        

	         <div class="dropdown">

		   <button class="dropbtn">IAAS</button>
			   <div class="dropdown-content">

                              <a href="https://github.com/charuchandak/myCloud/tree/master/newiaas.html">Remote OS</a>


					</div>		


	

		 </div> 

        

       	 	 <!-- IAAS button end-->

	                 

                 <!-- NAAS button -->

                 <div class="dropdown">

		  			  <button class="dropbtn">NAAS</button>

				 </div>

                 <!-- NAAS button end-->

                 

			</div>
        
    	<!-- menu end -->





"""
              

print """<div class="Heading">

<h1>We Have The Following Images </h1>

</div>
"""
a= commands.getoutput("sudo docker images")
b = a.splitlines()
i=0
l=len(b)
c=[]
d=[]

print "<table id='table' border=1>"
while i < l:
        t=" ".join(b[i].split())
        c.append(t)
        d.append(c[i].split(" "))
        i+=1

print "<tr><th>Available Image</th><th>Version</th></tr>"
i=1
l=len(d)
while i< l:
	print "<tr><td>"+d[i][0] + "</th><td>" + d[i][1]+"</td></tr>"
        i+=1

print "</table>"

print"""
<div class="Heading">
			
	<h3>Launch CONTAINERS of the available IMAGES</h3>
	
	<h3>enter no of container to launch</h3>

</div>
<div class="form">
	<form action='caas.py' >

	<input type='number' placeholder="enter no. of Containers" name='n'>	
	
	<button >Submit</button>

	</form>
</div>

<div class="Heading">
			
	<h3>OR</h3>
	
	<h3>You can choose from the following PACKAGES and COMMIT your own DOCKER IMAGE</h3>

	<h3>Select IMAGE</h3>

</div>	

<div class="docker-form">
			
<form action='docker-commit.py'>

"""
j=1
l=len(d)
while j< l:
	print "<input type='radio' name='image' value='{0}'>{0}</option>".format(d[j][0])
        j+=1

print"""
<div class="Heading">
<h2>-Select PACKAGES </h2>
</div>

<div class="checkbox"> 
<input type='checkbox' name='soft1' value='httpd'>Apache Server<br><br>
<input type='checkbox' name='soft2' value='ssh'>SSH Server<br><br>
<input type='checkbox' name='soft3' value='net'>net-tools<br><br>
<input type='checkbox' name='soft4' value='python'>python<br><br>
<input type='checkbox' name='soft5' value='nfs'>NFS Server<br><br>
</div>

<div class="heading">
<h4>enter name for your image</h4>
</div> 

<div class="form">
<input placeholder="docker name" name='dname'>
</div>

<div class="heading">
<h4>version</h4>
</div>

<div class="form">
<input placeholder="enter version" name='ver'>
</div>

<br>

<center><button>Submit</button></center>

</form>

</div>

<footer class="footer">
<p class="our-motto"><b>Use Anywhere On Any Ware</b></p>
	 

	<div class="footer_links">
				<a href="#">Home - </a>
				
				<a href="https://github.com/charuchandak/myCloud/tree/master/About_Us.html">About - </a>
				
				<a href="#">Faq - </a>
				
				<a href="https://github.com/charuchandak/myCloud/tree/master/Contact_us.html">Contact </a>
			
		
	</div>

<p class="Team-name">Red Sprites &copy; 2017</p>

</footer>
"""



# rittco_exercise
this is an excercise project using djnago framework
  the app requries library to run :
  * Django_countries : this library adds a country field for the applications form run the following command to get the library installed :</br>
 1)pip3 install django_countries
</br>

after installing the previous library you will need to run migrations to setup the database schema required by the internal modules on django (such as the admin module):
  1) cd recruitment/
  2) python3 manage.py migrate
  </br>
after running the migrations for internal modules you will need to make a migration for the custome made application (application) which is responsible for storing the user's submitted application :</br>
<ol>
<li> python3 manage.py makemigrations applications</li>
  <li> python3 manage.py migrate applications </li>
 <ol>
after running the previous migrations you can now run the server at a local environment, on your terminal run the following command :
<li>python3 manage.py runserver</li>
  
<p>the previous command will run a local server at port 8000 </p>
<ul>
   <li>to visit the server enter the following url in your browser : 127.0.0.1:8000 </li>
   <li>to submit an application follow the link (submit new application) in the broswer </li>
 </ul>
 
 
managing recieved applications :
the recruitment application is integrated with django's built-in admin feature, you can sign in as an administartor to manage recieved applications.
 
open another terminal and run the following command to make an admin user : 
  1) python manage.py createsuperuser. <br />
  the terminal will guide you through a sign up process (provide your credentials  (username , email and password)). <br />
  
  2) follow the (administrate application) link on the website and use the credntials you signed-up with. <br />
  3) go to the application link on the admin panel , you will see a list of submitted applications. <br />
  4) to accept an application , mark it with selected ,and then select (mark application as accepted) from the actions drop down menu and hit go. <br />
  5) to reject an application , mark it with selected ,and then select (mark application as rejected) from the actions drop down menu and hit go. <br />
  6) the status of the applications will be updated according to the action performed in the previous step.

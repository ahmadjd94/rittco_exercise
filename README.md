# rittco_exercise
this is an excercise project using djnago framework
  the app requries library to run :
  * Django_countries : this library adds a country field for the applications form run the following command to get the library installed : pip3 install django_countries


after installing the previous library you will need to run migrations to setup the database schema required by the internal modules on django (such as the admin module):
  cd recruitment/
  python3 manage.py migrate
  
after running the migrations for internal modules you will need to make a migration for the custome made application (application) which is responsible for storing the user's submitted application :
  python3 manage.py makemigrations applications
  python3 manage.py migrate applications
 after running the previous migrations you can now run the server at a local environment, on your terminal run the following command :
  python3 manage.py runserver
 the previous command will run a local server at port 8000 
  to visit the server enter the following url in your browser : 127.0.0.1:8000 
  to submit an application follow the link (submit new application) in the broswer 
  
  managing recieved applications :
  the recruitment application is integrated with django's built-in admin feature, you can sign in as an administartor to manage recieved applications 
 open another terminal and run the following command to make an admin user : 
  1) python manage.py createsuperuser
  the terminal will guide you through a sign up process (provide your credentials  (username , email and password))
  2) follow the (administrate application) link on the website and use the credntials you signed-up with
  3) go to the application link on the admin panel , you will see a list of submitted applications
  4) to accept an application , mark it with selected ,and then select (mark application as accepted) from the actions drop down menu and hit go
  5) to accept an application , mark it with selected ,and then select (mark application as accepted) from the actions drop down menu and hit go
  6) the status of the applications will be updated according to the action performed in the previous step
 

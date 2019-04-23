# chatroom

Python Chat Room with Socektio

In order to run this project, you need to make sure that all requirements are satisfied

this is the list of requirements

aniso8601==6.0.0
certifi==2019.3.9
cffi==1.12.3
chardet==3.0.4
Click==7.0
dnspython==1.16.0
eventlet==0.24.1
Flask==1.0.2
Flask-SocketIO==3.3.2
Flask-WTF==0.14.2
gevent==1.4.0
gevent-websocket==0.10.1
greenlet==0.4.15
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
monotonic==1.5
pycparser==2.19
PyJWT==1.7.1
python-engineio==3.5.1
python-socketio==4.0.0
pytz==2019.1
requests==2.21.0
six==1.12.0
SQLAlchemy==1.3.3
urllib3==1.24.2
Werkzeug==0.15.2
WTForms==2.2.1


this project uses virtual environment and Flask Blueprint to structure and creates the web server also Flask-SocketiO to implement the communication between the web browser and server and Flask Sqlalquemy to store the user in an SQLite database

to active the virtual enviroment go to the script folder and run active file under the folder \chatroom\venv\Scripts\

How to Run the server

after downloading or clone the repository, open CDM activate the virtual environment and then cd into chatroom folder and run the following command

python application.py then you can go to localhost:5000 on the web browser

**the users are stored in an SQLite database, the test users are

user: user1Chat pass: User1Chat
user: user2Chat pass: User2Chat**



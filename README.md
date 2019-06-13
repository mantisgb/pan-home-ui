# pan-home-ui
Simplified Web Interface for PAN-OS URL Category Profile

Project to demonstrate use of API to create a simple web interface to limited elements of PAN-OS configuration.

Assumes that you have installed Flask and Python on your system.

You will need to create a config.py file with the following variables relating to the test firewall you are working with
(I'm assuming you have a PAN-OS firewall running > v8.1 code). Obviously put actual values in the quotes :)
```
user = ""<br/>
pwd = ""<br/>
myip = ""<br/>
```

Flask wants an environment variable to define the app 
`export FLASK_APP=app.py`

Run the server (note the warning displayed about development only!)
`flask run --host=0.0.0.0i`

The --host switch will enable you to connect to the server from a remote host.

Connect using http://\<Server IP\>:5000/

The project assumes that you also have a PAN-OS based firewall that is the target of the API calls.
Modify app.py to suit your own testing environment. The file is also hardcoded with our test
IP address and username/password. Deal with it.

from flask import Flask, render_template,request
import os,subprocess
# import xml.etree.ElementTree as ET

app = Flask(__name__)
password="Pasquale123"

################################################################
## create API token and store as tag called pasq-vm in .panrc ##
################################################################
b="panxapi.py -t pasq-vm -h 10.14.0.4 -l pasquale:" + password + " -k >>~/.panrc"
os.system(b)

# Open file read-only (r) with all categories.
# Create a dictionary where the key is the category and value set Allow
# For reference the other available settings are allow, alert, block, continue, override
# Think need list of tuples with category and status currently have error about expecting integer not str
categories = []
with open("categories-file",'r') as cats:
   for line in cats:
      category = line.rstrip()
      categories.append((category,'Allow'))

@app.route("/")
@app.route("/index")
def index():
   return render_template("index.html",categories=categories)

@app.route('/commit')
def commit():
    b="panxapi.py -t pasq-vm -xr --sync -C '<commit></commit>'"
    os.system(b);
    print "commit done"
    return "nothing"

@app.route('/urlchange')
def urlchange():
    category=request.args.get('category')
    action = request.args.get('action')
    b="panxapi.py -t pasq-vm -S '<member>"+category+"</member>' \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles/url-filtering/entry[@name='test']/"+action+"\""
    os.system(b);
    return ""

# Now we query the VM for the URL categories values that are not set to allow.
# Note the API doesn't return categories set to allow
b="panxapi.py -t pasq-vm -pg \"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles/url-filtering/entry[@name='test']\""
c=subprocess.check_output(b, shell=True);
print c;

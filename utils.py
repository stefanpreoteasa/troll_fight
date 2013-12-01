
import time
import re

WAIT =  2 #constant for the s() function
def s():
	time.sleep(WAIT)

def n():
	print "\n"

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") #regex for determinig a correct user name. Add spaces?

def valid_username(name):
	return USER_RE.match(name)
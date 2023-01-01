# DDoS TCP-Flooder
This DDoS TCP Flood attack will exploit the three-way handshaking mechanism of the TCP connection establishment process, where the server will receive many requests for SYN packets without being responded to by the server.

<!-- Serangan DDoS TCP Flood ini akan mengeksploitasi mekanisme three-way handshaking dari proses pembentukan koneksi TCP, di mana server akan mendapatkan banyak permintaan paket-paket SYN tanpa sempat direspon oleh server. -->

# Description
This directory contains DDoS TCP Flooder scripts that you can use in a Linux environment.

## How to install?
1. $ ``git clone https://github.com/Kevlog/DDoS-FTP-Flooder``
2. $ ``cd DDoS-FTP-Flooder``
3. $ ``sudo apt install python3``
4. $ ``sudo apt install python3-pip``
5. $ ``pip3 install progressbar``
6. $ ``python3 attack.py``

### Suggestion for You
You can add except with a display like this for example "Stopping Attack!".

This is so that when the user closes the program (by pressing ctrl + c), the program can be closed neatly.

I'm still learning a lot about python programming, this program is also a recode from the [RCode777](https://github.com/RCode777) account. That way I still have a lot to learn python programming.

Alright, maybe that's enough. Thank you for your attention.
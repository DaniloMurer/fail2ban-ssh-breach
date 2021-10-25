import requests
import time
import os
import paramiko
import socks



def connect_to_ssh() : 
    # Linux only
    USERNAME = "test"
    HOST = 'danilojakob.ch'
    PORT = 22


    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("Connecting")

    ssh.connect(HOST, port=PORT, username=USERNAME, password="test", banner_timeout=200)


def get_current_ip():
    session = requests.session()

    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print(e)
    else:
        return r.text


def renew_tor_ip():
    os.system("sudo service tor restart")


if __name__ == "__main__":
    while True:
        #time.sleep(5)
        print(get_current_ip())
        #if counter == 3:
        #    counter = 0
        renew_tor_ip()
        connect_to_ssh()
        #counter += 1

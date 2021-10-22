import requests
import time
from stem import Signal
from stem.control import Controller
import os
import pwd
import socket
import socks
from ssh.session import Session
from ssh import options


def connect_to_ssh() : 
    # Linux only
    USERNAME = "jada"
    HOST = '192.168.56.101'
    PORT = 22

    my_socket = socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150, True)
    sock = my_socket.socksocket
    sock.connect((HOST, PORT))

    s = Session()
    s.options_set(options.HOST, HOST)
    s.options_set(options.USER, USERNAME)
    s.options_set(options.PASSWORD_AUTH, "//Danilu01//")
    s.options_set_port(PORT)
    s.set_socket(sock)
    s.connect()

    # Authenticate with agent
    s.userauth_agent(USERNAME)

    chan = s.channel_new()
    chan.open_session()
    chan.request_exec('echo me')
    size, data = chan.read()
    while size > 0:
        print(data.strip())
        size, data = chan.read()
    chan.close()

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
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="passport123")
        controller.signal(Signal.NEWNYM)


if __name__ == "__main__":
    for i in range(5):
        print(get_current_ip())
        renew_tor_ip()
        time.sleep(5)
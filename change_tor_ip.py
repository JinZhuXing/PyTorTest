from stem import Signal
from stem.control import Controller
import requests

# change tor ip
def change_tor_ip(tor_server_ip = 'localhost', service_port = 9050, control_port = 9051, control_password = 'my-tor-password'):
    with Controller.from_port(address = tor_server_ip, port = control_port) as controller:
        controller.authenticate(password = control_password)
        controller.signal(Signal.NEWNYM)
    
    # define proxy
    proxy_url = 'socks5://' + tor_server_ip + ':' + str(service_port)
    proxies = {
        'https': proxy_url,
        'http': proxy_url
    }

    # check changed ip
    try:
        current_ip = requests.get(
            url='http://icanhazip.com/',
            proxies=proxies,
            verify=False
        )
        ip = current_ip.text.rstrip("\n")
        print(ip)
    except Exception as e:
        print(e)

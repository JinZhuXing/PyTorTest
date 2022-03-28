import argparse
import sys
import requests
from change_tor_ip import change_tor_ip

# main process
def main(args):
    # get arguments
    tor_server_ip = args.tor_server_ip
    service_port = args.service_port
    control_port = args.control_port
    control_password = args.control_password
    test_url = args.test_url

    # define proxy
    proxy_url = 'socks5://' + tor_server_ip + ':' + str(service_port)
    proxies = {
        'https': proxy_url,
        'http': proxy_url
    }

    # define request header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,ja;q=0.4,und;q=0.3',
        'cache-control': 'no-cache'
    }

    # send request with tor
    while (True):
        try:
            response = requests.get(test_url, headers = headers, proxies = proxies, timeout = 30)
            print(response.text)
            print('Success ***********************************************')
        except Exception as e:
            print(e)
            print('Change IP ********')
            change_tor_ip(tor_server_ip, service_port, control_port, control_password)
            print('Retry')


# argument parser
def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--tor_server_ip', type = str,
                    help = 'tor server ip address', default = 'localhost')
    parser.add_argument('--service_port', type = int,
                    help = 'tor service port', default = 9050)
    parser.add_argument('--control_port', type = int,
                    help = 'tor control port', default = 9051)
    parser.add_argument('--control_password', type = str,
                    help = 'tor control password', default = 'my-tor-password')
    parser.add_argument('--test_url', type = str,
                    help = 'tor test url', default = 'https://www.stackoverflow.com')
    
    return (parser.parse_args(argv))


# start point
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))

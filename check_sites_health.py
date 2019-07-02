import whois
import argparse
import requests
from datetime import datetime, timedelta


def get_args():
    parser = argparse.ArgumentParser(description='Resize image.')
    parser.add_argument(
        'input',
        type=str,
        help='Input path to textfile with URLs.'
    )
    parser.add_argument(
        '-d',
        '--days',
        default=30,
        type=int,
        help='Input number of days to check payment.'
    )
    args = parser.parse_args()
    return args, parser


def load_urls4check(path, parser):
    with open(path, 'r') as urls_file:
        return urls_file.read().split('\n')



def is_server_respond_with_2xx(url):
    try:
        response = requests.get(url)
        return response.ok
    except requests.exceptions.ConnectionError:
        return False


def get_domain(url):
    domain = url.strip('http://')
    return domain


def get_domain_expiration_date(domain):
    try:
        response = whois.whois(domain)
        expiration_date = response.expiration_date
        if type(expiration_date) == list:
            expiration_date = expiration_date[1]
        return expiration_date
    except whois.parser.PywhoisError:
        return datetime.now()


def is_domain_paid(expiration_date, days):
    now = datetime.now()
    difference = expiration_date - now
    delta = timedelta(days)
    if difference >= delta:
        return True
    else:
        return False


if __name__ == '__main__':
    args, parser = get_args()
    path = args.input
    days = args.days
    try:
        urls = load_urls4check(path, parser)
    except FileNotFoundError:
        parser.error('File not found.')

    for url in urls:
        response = is_server_respond_with_2xx(url)
        domain = get_domain(url)
        expiration_date = get_domain_expiration_date(domain)
        payment = is_domain_paid(expiration_date, days)
        status = 'URL: {} ; Connection status: {}; Payment status: {}'.format(url, response, payment)
        print(status)

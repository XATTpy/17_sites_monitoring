from whois import whois
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
        return None


def get_domain_expiration_date(url):
    response = whois(url)
    expiration_date = response.expiration_date
    if type(expiration_date) == list:
        expiration_date = expiration_date[1]
    return expiration_date


def is_domain_paid(expiration_date, days):
    now = datetime.now()
    difference = expiration_date - now
    delta = timedelta(days)
    if difference >= delta:
        return 'Paid'
    else:
        return 'Not paid'


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
        if response:
            expiration_date = get_domain_expiration_date(url)
            payment = is_domain_paid(expiration_date, days)
            status = 'URL: {} , status: OK, {}'.format(url, payment)
        else:
            status = 'URL: {} , status: No connection'.format(url)
        print(status)

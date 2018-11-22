#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

from urllib import request
from urllib.parse import urlencode

API_DEV_KEY = ''

parser = argparse.ArgumentParser(description='Pastes to pastebin')

parser.add_argument('--expire', dest='api_paste_expire_date', action='store',
    choices=['N', '10M', '1H', '1D', '1M'],
    default='10M',
    help='Expiration time')

parser.add_argument('--language', dest='api_paste_format', action='store',
    default='text',
    help='Paste language (syntax highlighting)')

args = parser.parse_args()

params = {'api_dev_key': API_DEV_KEY, 'api_option': 'paste', 'api_paste_private': '1'}

params.update(args.__dict__)

params['api_paste_code'] = sys.stdin.read()

params_urlencoded = bytes(urlencode(params), encoding='utf-8')

resp = request.urlopen('http://pastebin.com/api/api_post.php', params_urlencoded)

sys.stdout.buffer.write(resp.read())
sys.stdout.buffer.write(b'\r\n')

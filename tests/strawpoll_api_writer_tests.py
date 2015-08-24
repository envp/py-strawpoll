from strawpoll import StrawpollAPIWriter

import requests

BASE_URL = 'https://strawpoll.me'
API_PATH = 'api/v2/polls'
ENDPOINT = '/'.join([BASE_URL, API_PATH])
BAD_POLL = {
    'title': '',
    'options': [

    ],
    'multi': False,
    'permissive': False,
    'captcha': False
}
GOOD_POLL = {
    'title': '',
    'options': [

    ],
    'multi': False,
    'permissive': False,
    'captcha': False
}


def test_successfull_post_has_same_data_as_posted():
    raise StandardError

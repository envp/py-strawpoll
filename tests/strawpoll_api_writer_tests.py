from strawpoll import StrawpollAPIWriter

import requests

BASE_URL = 'https://strawpoll.me'
API_PATH = 'api/v2/polls'
endpoint = '/'.join([BASE_URL, API_PATH])

poll = {
    'title': '',
    'options': [

    ],
}

def test_successfull_post_has_same_data_as_posted():
    raise StandardError

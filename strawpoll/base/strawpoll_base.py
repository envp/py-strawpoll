import re
import json
import requests


class StrawpollAPIBase(object):
    """
    TODO: Document this class
    """
    API_KEYWORDS = frozenset(
        [u'title', u'options', u'votes',
         u'multi', u'permissive', u'id', u'captcha'])

    API_ENDPOINT = 'https://strawpoll.me/api/v2/polls/'

    URL_PATTERN = re.compile('^https?://strawpoll.me/(?P<id>[1-9][0-9]*)/?r?')

    USER_AGENT = 'Strawpoll API Reader'

    API_POST_HEADERS = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'StrawpollAPIWriter'
    }

    def __init__():
        self.id = None
        self.title = None
        self.options = None
        self.votes = None
        self.multi = False
        self.permissive = False
        self.captcha = False

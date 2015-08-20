"""
A python module to provide methods to write data to Strawpoll's JSON API:
https://strawpoll.me/api/v2/polls

The StrawpollAPIWriter class provides methods for:
* Creating a poll instance
* POSTing data to strawpoll's API
"""

import requests
import json
import pprint


class StrawpollAPIWriter(object):
    """
    TODO: Document this class
    """
    # These are the attributes that strawpoll accepts in its API call
    # See: https://github.com/strawpoll/strawpoll/wiki/API
    # The strings have been marked utf-8 for compatibility with json.loads()
    API_KEYWORDS = frozenset(
        [u'title', u'options', u'votes',
         u'multi', u'permissive', u'id', u'captcha'])
    API_ENDPOINT = 'https://strawpoll.me/api/v2/polls'
    USER_AGENT = 'Strawpoll API Reader'
    API_POST_HEADERS = {
        'Content-Type': 'application/json',
        'X-Requested-With': 'StrawpollAPIWriter'
    }

    def __init__(self, data={}):
        """ Construct self using a dictionary of data """
        self.id = None
        self.title = None
        self.options = None
        self.votes = None
        self.multi = False
        self.permissive = False
        self.captcha = False

        for key in data.keys():
            if hasattr(self, key):
                setattr(self, key, data[key])

    def post(self):
        """
        Posts the strawpoll object to the strawpoll API and returns a
        Strawpoll object with a valid id attribute. Doesn't handle the case
        where a valid id already exists. If the post is successful a new
        object with overwritten id is returned
        """

        body = json.dumps(self.to_clean_dict())
        response = requests.post(self.API_ENDPOINT, data=body, headers=self.API_POST_HEADERS)
        return response.text

    def to_clean_dict(self):
        """
        Cleans up self.__dict__ so that it is accepted as json by strawpoll API
        """
        cdict = self.__dict__
        for key in cdict.keys():
            if cdict[key] == None:
                del cdict[key]
        return cdict

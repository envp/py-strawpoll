"""
A python module to provide the base class for Strawpoll's JSON API:
https://strawpoll.me/api/v2/polls

The StrawpollAPIWriter class provides methods for:
* Calculations on fetched poll data
* Fetching poll data is left to the reader class to define
"""
import re


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
        'X-Requested-With': 'StrawpollAPIWriter, github=http://git.io/vsV1E'
    }

    def __init__(self, data={}):
        self.id = None
        self.title = None
        self.options = None
        self.votes = None
        self.multi = False
        self.permissive = False
        self.captcha = False

        for key in data.keys():
            try:
                setattr(self, key, data[key])
            except AttributeError:
                continue

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # Begin instance methods
    def total_votes(self):
        """ Returns the sum of votes cast for all option in a strawpoll """
        return sum(self.votes)

    def normalize(self):
        """ Returns Normalized votes on a 0.0 - 1.0 scale """
        total = self.total_votes()
        return [vote / total for vote in self.votes]

    def votes_for(self, option):
        """
        Returns the number of votes an option recieved
        Return None if no such option exists
        """
        try:
            return self.votes[self.options.index(option)]
        except ValueError:
            return None

    def normalized_votes_for(self, option):
        """
        Returns the fraction of votes an option recieved
        Return None if no such option exists
        """
        return self.normalize()[self.options.index(option)]

    def winner(self):
        """ Returns the option that got the most votes """
        most_popular_index = self.votes.index(max(self.votes))
        return self.options[most_popular_index]

    def loser(self):
        """ Returns the option that got the least votes """
        least_popular_index = self.votes.index(min(self.votes))
        return self.options[least_popular_index]

    def to_clean_dict(self):
        """
        Cleans up self.__dict__ so that it is accepted as json by strawpoll API
        """
        cdict = self.__dict__
        for key in cdict.keys():
            if cdict[key] == None:
                del cdict[key]
        return cdict

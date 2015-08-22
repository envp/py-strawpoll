"""
A python module to provide methods to read data from existing polls using
Strawpoll's JSON API (https://strawpoll.me/api/v2/polls).

The StrawpollAPIReader class provides methods for:
* Capturing all poll data in an instance
* Performing basic options such as normalizing votes for each option
* Finding the winner / loser
"""

from __future__ import division
from base.strawpoll_base import StrawpollAPIBase

import requests
import json


class StrawpollAPIReader(StrawpollAPIBase):
    """
    TODO: Document this class
    """
    def __init__(self, data=None):
        """ Construct self using a dictionary of data """
        super(StrawpollAPIBase, self).__init__()
        for key in data.keys():
            # This actually worked.
            # hasattr -> setattr died with AttributeErrors
            try:
                setattr(self, key, data[key])
            except AttributeError:
                # Log this?
                continue
    #
    # @classmethod
    # def from_json(cls, json_string):
    #     """ See StrawpollAPIBase.from_json(json_string) """
    #     return super(StrawpollAPIReader, cls).from_json(json_string)
    #
    # @classmethod
    # def from_apiv2(cls, id):
    #     """ See StrawpollAPIBase.from_apiv2(id) """
    #     return super(StrawpollAPIReader, cls).from_apiv2(id)
    #
    # @classmethod
    # def from_url(cls, url):
    #     """ See StrawpollAPIBase.from_url(url) """
    #     return super(StrawpollAPIReader, cls).from_url(url)
    #
    # # Begin instance methods
    # def total_votes(self):
    #     """ See StrawpollAPIBase.total_votes() """
    #     return super(StrawpollAPIReader, self).total_votes()
    #
    # def normalize(self):
    #     """ See StrawpollAPIBase.normalize() """
    #     return super(StrawpollAPIReader, self).normalize()
    #
    # def votes_for(self, option):
    #     """ See StrawpollAPIBase.votes_for(option) """
    #     return super(StrawpollAPIReader, self).votes_for(option)
    #
    # def normalized_votes_for(self, option):
    #     """ See StrawpollAPIBase.normalized_votes_for(option) """
    #     return super(StrawpollAPIReader, self).normalized_votes_for(option)
    #
    # def winner(self):
    #     """ See StrawpollAPIBase.winner() """
    #     return super(StrawpollAPIReader, self).winner()
    #
    # def loser(self):
    #     """ See StrawpollAPIBase.loser() """
    #     return super(StrawpollAPIReader, self).loser()

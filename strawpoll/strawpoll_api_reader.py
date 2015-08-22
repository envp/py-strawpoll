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

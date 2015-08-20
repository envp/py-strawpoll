import strawpoll
import pprint
import json


if __name__ == '__main__':
    sp = strawpoll.StrawpollAPIReader.from_apiv2(1)
    pprint.pprint(sp.votes)

__author__ = 'wy'
__doc__ = '''对放入redis的url去重'''

from qx.qyxc.utils import Redis_utils


class Dupefilter(object):


    @staticmethod
    def request_seen(url):
        # This returns the number of values added, zero if already exists.
        added = Redis_utils.server.sadd('url_dupefilter', url)

        if added == 0:
            return 1
        else:
            return 0
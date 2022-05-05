from cubics.modules import instruction, resource
from cubics.library import models, utils
from cubics.library.config import config


def read(key, time, args={}):
    """
    Read statistic by key and time
    """
    return resource.read(**{**{
        'type': 'statistic',
        'key': key,
        'sort': 'time',
        'sortValue': time,
    }, **args})

def scan(key, time=None, args={}):
    """
    Scan statistics by key, sort by time
    """
    return resource.scan(**{**{
        'type': 'statistic',
        'index': None,
        'indexValue': None,
        'sort': 'time',
        'sortValue': time,
        'keyValue': key,
    }, **args})
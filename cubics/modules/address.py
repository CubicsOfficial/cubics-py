from cubics.library import utils
from cubics.library.config import config


def read(address):
    """
    Read address data (balance, profile, pool, token)
    """
    return utils.request(
        method='GET',
        url=config['interface']+'/profile',
        params={
            'address': address,
            'dev': config['dev'],
            'identity': config['identity'],
        })
from cubics.modules import instruction, resource
from cubics.library import models, utils, hashed
from cubics.library.config import config


def read(hash, args={}):
    """
    Read balance by hash
    """
    return resource.read(**{**{
        'type': 'balance',
        'key': hash,
    }, **args})

def readOwnerToken(owner, token, args={}):
    """
    Read balance by owner and token
    """
    return resource.read(**{**{
        'type': 'balance',
        'key': hashed.balance({'owner': owner, 'token': token}),
    }, **args})

def list(hashes, args={}):
    """
    List balances by hashes
    """
    return resource.list(**{**{
        'type': 'balance',
        'keys': hashes,
    }, **args})

def scanOwnerAmount(owner, amount=None, hash=None, args={}):
    """
    Scan balances by owner, sort by amount
    """
    return resource.scan(**{**{
        'type': 'balance',
        'index': 'owner',
        'indexValue': owner,
        'sort': 'amount',
        'sortValue': amount,
        'keyValue': hash,
    }, **args})

def scanTokenAmount(token, amount=None, hash=None, args={}):
    """
    Scan balances by token, sort by amount
    """
    return resource.scan(**{**{
        'type': 'balance',
        'index': 'token',
        'indexValue': token,
        'sort': 'amount',
        'sortValue': amount,
        'keyValue': hash,
    }, **args})
from cubics.modules import instruction, resource
from cubics.library import models, utils, hashed
from cubics.library.config import config


def update(spender, token, amount, tx={}):
    """
    Update allowance for spender address
    """
    return instruction.wrap({
        'function': 'allowance.update',
        'spender': spender,
        'token': token,
        'amount': utils.amount(amount),
    }, tx)

def read(hash, args={}):
    """
    Read allowance by hash
    """
    return resource.read(**{**{
        'type': 'allowance',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List allowances by hashes
    """
    return resource.list(**{**{
        'type': 'allowance',
        'keys': hashes,
    }, **args})

def readCreatorSpenderToken(creator, spender, token, args={}):
    """
    Read allowance by creator, spender, and token
    """
    return resource.read(**{**{
        'type': 'allowance',
        'key': hashed.allowance({'creator': creator, 'spender': spender, 'token': token}),
    }, **args})

def list(hashes, args={}):
    """
    List allowances by hashes
    """
    return resource.list(**{**{
        'type': 'allowance',
        'keys': hashes,
    }, **args})

def scanCreatorCreated(creator, created=None, hash=None, args={}):
    """
    Scan allowances by creator, sort by created
    """
    return resource.scan(**{**{
        'type': 'allowance',
        'index': 'creator',
        'indexValue': creator,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanSpenderCreated(spender, created=None, hash=None, args={}):
    """
    Scan allowances by spender, sort by created
    """
    return resource.scan(**{**{
        'type': 'allowance',
        'index': 'spender',
        'indexValue': spender,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})
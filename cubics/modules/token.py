from cubics.modules import instruction, resource
from cubics.library import models, utils, hashed
from cubics.library.config import config


def create(name, symbol=None, supply=None, reserve=None, whole=None, description=None, links=None, meta=None, preview=None, owner=None, frozen=None, category=None, object=None, content=None, mime=None, tx={}):
    """
    Create token
    """
    return instruction.wrap({
        'function': 'token.create',
        'name': name,
        'symbol': symbol,
        'supply': utils.amount(supply),
        'reserve': utils.amount(reserve),
        'whole': whole,
        'description': description,
        'links': links,
        'meta': meta,
        'preview': preview,
        'owner': owner,
        'frozen': frozen,
        'category': category,
        'object': object,
        'content': content,
        'mime': mime,
    }, tx)

def update(token, name=None, description=None, links=None, meta=None, preview=None, frozen=None, category=None, mime=None, tx={}):
    """
    Update specified values of an token
    """
    return instruction.wrap({
        'function': 'token.update',
        'token': token,
        'name': name,
        'description': description,
        'links': links,
        'meta': meta,
        'preview': preview,
        'frozen': frozen,
        'category': category,
        'mime': mime,
    }, tx)

def mint(token, amount, tx={}):
    """
    Mint from reserve
    """
    return instruction.wrap({
        'function': 'token.mint',
        'token': token,
        'amount': utils.amount(amount),
    }, tx)

def read(hash, args={}):
    """
    Read token by hash
    """
    return resource.read(**{**{
        'type': 'token',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List tokens by hashes
    """
    return resource.list(**{**{
        'type': 'token',
        'keys': hashes,
    }, **args})

def scanCreatorCreated(creator, created=None, hash=None, args={}):
    """
    Scan tokens by creator, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'creator',
        'indexValue': creator,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanNameCreated(name, created=None, hash=None, args={}):
    """
    Scan tokens by name, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'name',
        'indexValue': name,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanSymbolCreated(symbol, created=None, hash=None, args={}):
    """
    Scan tokens by symbol, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'symbol',
        'indexValue': symbol,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanOwnerCreated(owner, created=None, hash=None, args={}):
    """
    Scan tokens by owner, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'owner',
        'indexValue': owner,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanContentCreated(content, created=None, hash=None, args={}):
    """
    Scan tokens by content, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'content',
        'indexValue': content,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanOwnerCategoryCreated(owner, category, created=None, hash=None, args={}):
    """
    Scan tokens by owner and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'ownerCategory',
        'indexValue': hashed.values([owner, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanCreatorCategoryCreated(creator, category, created=None, hash=None, args={}):
    """
    Scan tokens by creator and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'token',
        'index': 'creatorCategory',
        'indexValue': hashed.values([creator, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})
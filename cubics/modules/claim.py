from cubics.modules import instruction, resource
from cubics.library import models, utils, hashed
from cubics.library.config import config


def create(owner, token, tokenAmount, baseAmount=None, expires=None, unlocks=None, frozen=None, category=None, meta=None, answer=None, number=None, tx={}):
    """
    Create claim
    """
    return instruction.wrap({
        'function': 'claim.create',
        'owner': owner,
        'token': token,
        'tokenAmount': utils.amount(tokenAmount),
        'baseAmount': utils.amount(baseAmount),
        'expires': expires,
        'unlocks': unlocks,
        'frozen': frozen,
        'category': category,
        'meta': meta,
        'answer': answer,
        'number': number,
    }, tx)

def update(claim, tokenAmount=None, baseAmount=None, expires=None, unlocks=None, frozen=None, category=None, meta=None, answer=None, number=None, tx={}):
    """
    Update claim
    """
    return instruction.wrap({
        'function': 'claim.update',
        'claim': claim,
        'tokenAmount': utils.amount(tokenAmount),
        'baseAmount': utils.amount(baseAmount),
        'expires': expires,
        'unlocks': unlocks,
        'frozen': frozen,
        'category': category,
        'meta': meta,
        'answer': answer,
        'number': number,
    }, tx)

def transfer(claim, to, tx={}):
    """
    Transfer claim
    """
    return instruction.wrap({
        'function': 'claim.transfer',
        'claim': claim,
        'to': to,
    }, tx)

def resolve(claim, tx={}):
    """
    Resolve claim
    """
    return instruction.wrap({
        'function': 'claim.resolve',
        'claim': claim,
    }, tx)

def read(hash, args={}):
    """
    Read claim by hash
    """
    return resource.read(**{**{
        'type': 'claim',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List claims by hashes
    """
    return resource.list(**{**{
        'type': 'claim',
        'keys': hashes,
    }, **args})

def scanHolderCategoryCreated(holder, category, created=None, hash=None, args={}):
    """
    Scan claims by holder and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'holderCategory',
        'indexValue': hashed.values([holder, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanIssuerCategoryCreated(issuer, category, created=None, hash=None, args={}):
    """
    Scan claims by issuer and category, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuerCategory',
        'indexValue': hashed.values([issuer, category])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanIssuerAnswer(issuer, answer=None, hash=None, args={}):
    """
    Scan claims by issuer, sort by answer
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuer',
        'indexValue': hashed.values([issuer])[-8:],
        'sort': 'answer',
        'sortValue': answer,
        'keyValue': hash,
    }, **args})

def scanIssuerNumber(issuer, number=None, hash=None, args={}):
    """
    Scan claims by issuer, sort by number
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuer',
        'indexValue': hashed.values([issuer])[-8:],
        'sort': 'number',
        'sortValue': number,
        'keyValue': hash,
    }, **args})

def scanIssuerTokenAmount(issuer, tokenAmount=None, hash=None, args={}):
    """
    Scan claims by issuer, sort by tokenAmount
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuer',
        'indexValue': hashed.values([issuer])[-8:],
        'sort': 'tokenAmount',
        'sortValue': tokenAmount,
        'keyValue': hash,
    }, **args})

def scanIssuerBaseAmount(issuer, baseAmount=None, hash=None, args={}):
    """
    Scan claims by issuer, sort by baseAmount
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuer',
        'indexValue': hashed.values([issuer])[-8:],
        'sort': 'baseAmount',
        'sortValue': baseAmount,
        'keyValue': hash,
    }, **args})

def scanIssuerCreated(issuer, created=None, hash=None, args={}):
    """
    Scan claims by issuer, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuer',
        'indexValue': hashed.values([issuer])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanHolderCreated(holder, created=None, hash=None, args={}):
    """
    Scan claims by holder, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'holder',
        'indexValue': hashed.values([holder])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanIssuerTokenCreated(issuer, token, created=None, hash=None, args={}):
    """
    Scan claims by issuer and token, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuerToken',
        'indexValue': hashed.values([issuer, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanHolderTokenCreated(holder, token, created=None, hash=None, args={}):
    """
    Scan claims by holder and token, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'holderToken',
        'indexValue': hashed.values([holder, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanIssuerHolder(issuer, holder, created=None, hash=None, args={}):
    """
    Scan claims by issuer and holder, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuerHolder',
        'indexValue': hashed.values([issuer, holder])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanIssuerHolderToken(issuer, holder, token, created=None, hash=None, args={}):
    """
    Scan claims by issuer, holder and token, sort by created
    """
    return resource.scan(**{**{
        'type': 'claim',
        'index': 'issuerHolderToken',
        'indexValue': hashed.values([issuer, holder, token])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})
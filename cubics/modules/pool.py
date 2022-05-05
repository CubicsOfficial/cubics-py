from cubics.programs import auction, launch, lending, lock, loot, lottery, royalty, staking, swap, vote
from cubics.modules import instruction, resource
from cubics.library import models, utils, hashed
from cubics.library.config import config


def create(token, program, name=None, description=None, type=None, candidates=None, rate=None, percentage=None, number=None, expires=None, answers=None, meta=None, minAmount=None, maxAmount=None, minTime=None, maxTime=None, transfersLimit=None, claimsLimit=None, tokenLimit=None, baseLimit=None, tokenTarget=None, baseTarget=None, tx={}):
    """
    Create pool
    """
    return instruction.wrap({
        'function': 'pool.create',
        'token': token,
        'program': program,
        'name': name,
        'description': description,
        'type': type,
        'candidates': candidates,
        'rate': rate,
        'percentage': percentage,
        'number': number,
        'expires': expires,
        'answers': answers,
        'meta': meta,
        'minAmount': utils.amount(minAmount),
        'maxAmount': utils.amount(maxAmount),
        'minTime': minTime,
        'maxTime': maxTime,
        'transfersLimit': transfersLimit,
        'claimsLimit': claimsLimit,
        'tokenTarget': utils.amount(tokenTarget),
        'tokenLimit': utils.amount(tokenLimit),
        'baseTarget': utils.amount(baseTarget),
        'baseLimit': utils.amount(baseLimit),
    }, tx)

def instance(hash, args={}):
    """
    Get pool by hash
    Return as program instance
    """
    pool = read(hash, args)
    if not pool: return
    instance = getattr(globals()[pool['program']], pool['program'].capitalize())
    return instance(pool)

def read(hash, args={}):
    """
    Read pool by hash
    """
    return resource.read(**{**{
        'type': 'pool',
        'key': hash,
    }, **args})

def list(hashes, args={}):
    """
    List pools by hashes
    """
    return resource.list(**{**{
        'type': 'pool',
        'keys': hashes,
    }, **args})

def scanTokenProgramCreated(token, program, created=None, hash=None, args={}):
    """
    Scan pools by token and program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'tokenProgram',
        'indexValue': hashed.values([token, program])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanCreatorProgramCreated(creator, program, created=None, hash=None, args={}):
    """
    Scan pools by creator and program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'creatorProgram',
        'indexValue': hashed.values([creator, program])[-8:],
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanNameCreated(name, created=None, hash=None, args={}):
    """
    Scan pools by name, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'name',
        'indexValue': name,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanCreatorCreated(creator, created=None, hash=None, args={}):
    """
    Scan pools by creator, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'creator',
        'indexValue': creator,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})


def scanProgramCreated(program, created=None, hash=None, args={}):
    """
    Scan pools by active program, sort by created
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'created',
        'sortValue': created,
        'keyValue': hash,
    }, **args})

def scanProgramExpires(program, expires=None, hash=None, args={}):
    """
    Scan pools by active program, sort by expires
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'expires',
        'sortValue': expires,
        'keyValue': hash,
    }, **args})

def scanProgramNumber(program, number=None, hash=None, args={}):
    """
    Scan pools by active program, sort by number
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'number',
        'sortValue': number,
        'keyValue': hash,
    }, **args})

def scanProgramBaseBalance(program, baseBalance=None, hash=None, args={}):
    """
    Scan pools by active program, sort by balance
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'baseBalance',
        'sortValue': baseBalance,
        'keyValue': hash,
    }, **args})

def scanProgramTokenBalance(program, tokenBalance=None, hash=None, args={}):
    """
    Scan pools by active program, sort by tokenBalance
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'tokenBalance',
        'sortValue': tokenBalance,
        'keyValue': hash,
    }, **args})

def scanProgramTransfersCount(program, transfersCount=None, hash=None, args={}):
    """
    Scan pools by active program, sort by transfersCount
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'transfersCount',
        'sortValue': transfersCount,
        'keyValue': hash,
    }, **args})

def scanProgramType(program, type=None, hash=None, args={}):
    """
    Scan pools by active program, sort by type
    """
    return resource.scan(**{**{
        'type': 'pool',
        'index': 'activeProgram',
        'indexValue': program,
        'sort': 'type',
        'sortValue': type,
        'keyValue': hash,
    }, **args})
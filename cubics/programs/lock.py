from cubics.modules import instruction
from cubics.library import utils


class Lock():
    """
    Lock pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, unlocks=None, expires=None, owner=None, tx={}):
        """
        Transfer to lock pool
        """
        return instruction.wrap({
            'function': 'lock.transfer',
            'pool': self.pool['hash'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
            'expires': expires,
            'owner': owner,
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from lock pool
        """
        return instruction.wrap({
            'function': 'lock.claim',
            'pool': self.pool['hash'],
            'claim': claim,
        }, tx)
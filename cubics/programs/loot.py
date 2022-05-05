from cubics.modules import instruction
from cubics.library import utils


class Loot():
    """
    Loot pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, tx={}):
        """
        Transfer to loot pool
        """
        return instruction.wrap({
            'function': 'loot.transfer',
            'pool': self.pool['hash'],
        }, tx)

    def deposit(self, token, unlocks=None, tx={}):
        """
        Deposit nft to loot pool
        """
        return instruction.wrap({
            'function': 'loot.deposit',
            'pool': self.pool['hash'],
            'token': token,
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw nft from loot pool
        """
        return instruction.wrap({
            'function': 'loot.withdraw',
            'pool': self.pool['hash'],
            'claim': claim,
        }, tx)

    def clear(self, tx={}):
        """
        Clear loot pool
        """
        return instruction.wrap({
            'function': 'loot.clear',
            'pool': self.pool['hash'],
        }, tx)
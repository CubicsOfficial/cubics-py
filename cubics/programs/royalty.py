from cubics.modules import instruction
from cubics.library import utils


class Royalty():
    """
    Royalty pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, tx={}):
        """
        Claim from royalty pool
        """
        return self.claim(token, tx)

    def claim(self, token, tx={}):
        """
        Claim from royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.claim',
            'pool': self.pool['hash'],
            'token': token,
        }, tx)

    def deposit(self, amount, unlocks=None, tx={}):
        """
        Deposit to royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.deposit',
            'pool': self.pool['hash'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw from royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.withdraw',
            'pool': self.pool['hash'],
            'claim': claim,
        }, tx)

    def close(self, tx={}):
        """
        Close royalty pool
        """
        return instruction.wrap({
            'function': 'royalty.close',
            'pool': self.pool['hash'],
        }, tx)
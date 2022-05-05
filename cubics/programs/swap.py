from cubics.modules import instruction
from cubics.library import utils


class Swap():
    """
    Swap pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, token, amount, tx={}):
        """
        Transfer to swap pool
        """
        return instruction.wrap({
            'function': 'swap.transfer',
            'pool': self.pool['hash'],
            'token': token,
            'amount': utils.amount(amount),
        }, tx)

    def deposit(self, tokenAmount, baseAmount, unlocks=None, tx={}):
        """
        Deposit to swap pool
        """
        return instruction.wrap({
            'function': 'swap.deposit',
            'pool': self.pool['hash'],
            'tokenAmount': utils.amount(tokenAmount),
            'baseAmount': utils.amount(baseAmount),
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, percentage=1, tx={}):
        """
        Withdraw from swap pool
        """
        assert percentage <= 1, 'percentage:invalid'

        return instruction.wrap({
            'function': 'swap.withdraw',
            'pool': self.pool['hash'],
            'claim': claim,
            'percentage': percentage,
        }, tx)
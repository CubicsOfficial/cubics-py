from cubics.modules import instruction
from cubics.library import utils


class Auction():
    """
    Auction pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, tx={}):
        """
        Transfer to auction pool
        """
        return instruction.wrap({
            'function': 'auction.transfer',
            'pool': self.pool['hash'],
            'amount': utils.amount(amount),
        }, tx)

    def deposit(self, unlocks=None, tx={}):
        """
        Deposit to auction pool
        """
        return instruction.wrap({
            'function': 'auction.deposit',
            'pool': self.pool['hash'],
            'unlocks': unlocks,
        }, tx)

    def resolve(self, tx={}):
        """
        Resolve auction pool
        """
        return instruction.wrap({
            'function': 'auction.resolve',
            'pool': self.pool['hash'],
        }, tx)

    def cancel(self, tx={}):
        """
        Cancel auction pool
        """
        return instruction.wrap({
            'function': 'auction.cancel',
            'pool': self.pool['hash'],
        }, tx)

    def close(self, tx={}):
        """
        Close auction pool
        """
        return instruction.wrap({
            'function': 'auction.close',
            'pool': self.pool['hash'],
        }, tx)
from cubics.modules import instruction
from cubics.library import utils


class Launch():
    """
    Launch pool class
    """
    def __init__(self, pool):
        """
        Init pool
        """
        self.pool = pool

    def transfer(self, amount, tx={}):
        """
        Transfer to launch pool
        """
        return instruction.wrap({
            'function': 'launch.transfer',
            'pool': self.pool['hash'],
            'amount': utils.amount(amount),
        }, tx)

    def resolve(self, tx={}):
        """
        Resolve launch pool
        """
        return instruction.wrap({
            'function': 'launch.resolve',
            'pool': self.pool['hash'],
            'token': self.pool['token'],
        }, tx)

    def claim(self, claim, tx={}):
        """
        Claim from launch pool
        """
        return instruction.wrap({
            'function': 'launch.claim',
            'pool': self.pool['hash'],
            'claim': claim,
        }, tx)

    def deposit(self, amount, unlocks=None, tx={}):
        """
        Deposit to launch pool
        """
        return instruction.wrap({
            'function': 'launch.deposit',
            'pool': self.pool['hash'],
            'amount': utils.amount(amount),
            'unlocks': unlocks,
        }, tx)

    def withdraw(self, claim, tx={}):
        """
        Withdraw from launch pool
        """
        return instruction.wrap({
            'function': 'launch.withdraw',
            'pool': self.pool['hash'],
            'claim': claim,
        }, tx)

    def close(self, tx={}):
        """
        Close launch pool
        """
        return instruction.wrap({
            'function': 'launch.close',
            'pool': self.pool['hash'],
        }, tx)
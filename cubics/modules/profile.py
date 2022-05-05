from cubics.modules import instruction, resource
from cubics.library import models, utils
from cubics.library.config import config


def update(name=None, description=None, links=None, meta=None, preview=None, category=None, tx={}):
    """
    Update (or create) profile
    """
    return instruction.wrap({
        'function': 'profile.update',
        'name': name,
        'description': description,
        'links': links,
        'meta': meta,
        'preview': preview,
        'category': category,
    }, tx)
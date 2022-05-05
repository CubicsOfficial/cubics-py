from cubics.modules import instruction, resource
from cubics.library import models, utils
from cubics.library.config import config


def init(publicKey, privateKey=None):
    """
    Set public and private key
    """
    global config

    config['publicKey'] = publicKey
    config['privateKey'] = privateKey
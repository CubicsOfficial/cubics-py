import hashlib
import json 
from cubics.library.crypto import b58encode, b58decode

def values(values, base=None):
    """
    JSON encode array of values
    Apply sha256 to JSON values
    Return as base58 encoded string
    """
    enc = hashlib.sha256(json.dumps(values, separators=(',', ':')).encode()).digest()
    return b58encode(enc).decode()

def transaction(body):
    """
    Hash transaction body
    """
    return values([
        body.get('sender'),
        body.get('instructions'),
        body.get('nonce')])

def allowance(body):
    """
    Hash allowance body
    """
    return values([
        body.get('address'),
        body.get('spender'),
        body.get('token')])

def balance(body):
    """
    Hash balance body
    """
    return values([
        body.get('address'),
        body.get('token')])

def string(body, double=True):
    """
    Hash string
    Sha256(sha256(body))
    """
    enc = hashlib.sha256(body.encode()).digest()
    if double: enc = hashlib.sha256(enc).digest()
    return b58encode(enc).decode()

def inverse(hash):
    """
    Returns inverse/mirror hash
    """
    dec = list(bytearray(b58decode(hash)))
    return b58encode(bytes(dec[::-1])).decode()
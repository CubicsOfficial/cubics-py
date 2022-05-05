config = {
    'publicKey': None,
    'privateKey': None,
    'account': None,
    'secret': None,
    'dev': None,
    'identity': None,
    'network': 'https://network.cubics.com',
    'interface': 'https://interface.cubics.com',
    'zero': '11111111111111111111111111111111',
    'cubics': '111111111111111111111111111111cx',
    'dollar': '111111111111111111111111111111cd',
    'factory': '11111111111111111111111111factory',
    'sponsored': '1111111111111111111111111sponsored',
    'consumed': '11111111111111111111111111consumed',
}

def init(network=None, interface=None, dev=None):
    """
    Set endpoints and environment mode
    """
    global config

    if network: config['network'] = network
    if interface: config['interface'] = interface
    if dev is not None: config['dev'] = dev if dev else None
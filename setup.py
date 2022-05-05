# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path

setup(**{
    'name': 'cubics',
    'version': '0.9.1',
    'description': 'Official Python client for Cubics',
    'long_description': (Path(__file__).parent/'README.md').read_text(),
    'long_description_content_type': 'text/markdown',
    'author': 'Cubics',
    'author_email': 'contact@cubics.com',
    'url': 'https://github.com/CubicsOfficial/cubics-py',
    'packages': ['cubics', 'cubics.library', 'cubics.modules', 'cubics.programs'],
    'install_requires': ['requests', 'ed25519', 'scrypt'],
})
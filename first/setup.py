try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'First Python Project',
    'author': 'Nathan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nathanpguenther@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['first'],
    'scripts': ['bin/firstscript.py'],
    'name': 'first'
}

setup(**config)

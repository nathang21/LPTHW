try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Nathan Guenther',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nathanpguenther@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose', 'py.test'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)

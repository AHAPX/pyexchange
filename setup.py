from distutils.core import setup


setup(
    name = 'pyexchange',
    version = '0.5',
    description="Maker pyexchange library",
    author = 'MakerDAO',
    url = 'https://github.com/AHAPX/pyexchange',
    install_requires=[
        'pytz',
        'web3==3.16.4',
        'eth-testrpc==1.3.0',
        'requests==2.18.4',
        'appdirs==1.4.3',
        'tinydb==3.7.0',
        'filelock==3.0.0',
        'python-dateutil==2.6.1'
    ],
    keywords = ['crypto', 'trading'],
)

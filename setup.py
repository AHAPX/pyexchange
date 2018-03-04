from distutils.core import setup


setup(
    name = 'pyexchange',
    packages = ['pyexchange'],
    package_dir={'pyexchange': '.'},
    version = '0.1',
    description = 'Python lib for bx.in.th market',
    author = 'MakerDAO',
    url = 'https://github.com/AHAPX/pyexchange',
    download_url = 'https://github.com/AHAPX/pyexchange/archive/0.1.tar.gz',
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
    classifiers = [],
)

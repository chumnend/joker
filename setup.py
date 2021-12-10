import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_swagger',
    'waitress',
]

dev_require = [
    'black',
    'WebTest',
    'pyramid_debugtoolbar',
    'pytest',
    'pytest-cov',
]

setup(
    name='joker',
    version='0.2.0',
    description='joker',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Nicholas Chumney',
    author_email='nicholas.chumney@outlook.com',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'dev': dev_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = joker:main',
        ],
    },
)

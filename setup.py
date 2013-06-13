from distutils.core import setup

setup(
    name='BCCPrice',
    version='0.1.0',
    author='brmorris',
    author_email='bdm@outlook.com',
    packages=['BCCPrice'], # todo include test stuff here eg 'towelstuff.test'
    scripts=['bin/bcprice'],
    url='http://example.com/bcprice',
    license='LICENSE.txt',
    description='Command line interface to bitcoin prices via the bitcoincharts.com api',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 1.2.3",
        "requests-cache == 0.4.0",
    ],
)
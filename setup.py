from distutils.core import setup

setup(
    name='bcprice',
    version='0.5.0',
    author='brmorris',
    author_email='bdm@outlook.com',
#    packages=['lib'], 

    package_dir = {'': 'lib'}, 
    scripts=['bin/bcprice'],
    url='https://github.com/brmorris/bcprice',
    license='LICENSE.txt',
    description='Command line interface to bitcoin prices via the bitcoincharts.com api',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 1.2.3",
        "requests-cache == 0.4.0",
    ],
)

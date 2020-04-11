'''Setup Script for coronaupdates'''
from distutils.core import setup

setup(
    name='coronaupdates',         # How you named your package folder (MyLib)
    packages=['coronaupdates'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Command Line Interface for retrieving CoViD-19 related informations.',
    author='Arjun Adhikari',                   # Type in your name
    author_email='mailarjunadhikari@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/thearjun/coronaupdates',
    # I explain this later on
    download_url='https://github.com/theArjun/coronaupdates/archive/v1.0.0.tar.gz',
    keywords=['covid', 'coronaupdates', 'corona', 'virus',
              'pandemic'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'pandas',
        'lxml',
        'requests',
        'tabulate',
        'bs4',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package.
        'Development Status :: 3 - Alpha',

        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',   # Again, pick a license

        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

# from cx_Freeze import setup, Executable
# setup(name='pythonCX_Freeze',
#       version='0.1',
#       description='Retrie CoViD-19 updates by scraping and' \
#                   ' dividing into world, countries and continents.',
#       executables=[Executable('pythoncx_freeze.py')])

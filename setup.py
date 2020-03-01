import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

NAME = 'radiolist'
VERSION = '0.1'

try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except:
    long_description = ''

setup(name=NAME,
      version=VERSION,
      description='',
      long_description=long_description,
      author='b42',
      author_email='b42@srck.net',
      license='WTFPL',
      url='https://github.com/hackerspace/radiolist',
      scripts=[
            'radio_update'
          , 'radio'
          ],

      classifiers=[
            'Development Status :: 5 - Production/Stable'
          , 'Intended Audience :: End Users/Desktop'
          , 'Operating System :: OS Independent'
          , 'Programming Language :: Python'
          , 'Topic :: Multimedia :: Sound/Audio :: Players'
          ],
      )

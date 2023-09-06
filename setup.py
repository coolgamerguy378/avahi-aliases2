#/usr/bin/env python3
import os
from setuptools import (
  setup,
  find_packages,
)
import python3-avahi as app

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "python3-avahi",
    version = __import__('python3-avahi').__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Linux :: Ubuntu',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
    ),

    author='Jake Buck',
    author_email='Jake@378innovations.com',
    url='http://github.com/coolgamerguy378/avahi-aliases2',

    description='''Simple python application that manages the announcement of multiple avahi aliases''',
    long_description = read('README'),
    install_requires = [
        'python-daemon',
    ],
    packages = find_packages(),
    scripts = [
        'python3-avahi/bin/python3-avahi',
    ],
    data_files = [
        ('/etc/init/',              ['avahi_aliases/etc/init/python3-avahi.conf'] ),
        ('/etc/avahi/',             ['avahi_aliases/etc/avahi/aliases']),
        ('/etc/avahi/aliases.d/',   ['avahi_aliases/etc/avahi/aliases.d/default']),
    ],
    zip_safe = False,
)

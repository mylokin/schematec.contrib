import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = ''

setup(
    name='schematec.contrib',
    packages=find_packages(),
    # package_data={'': ['LICENSE']},
    version='0.1.0',
    namespace_packages=['schematec', 'schematec.contrib'],
    include_package_data = True,
    description='',
    author='Andrey Gubarev',
    author_email='mylokin@me.com',
    url='https://github.com/mylokin/schematec.contrib',
    keywords=['schema'],
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
    ),
)

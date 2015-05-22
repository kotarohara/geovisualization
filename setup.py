from setuptools import setup, find_packages
import os

import geovisualization

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='geovisualization',
    version=0.1,
    url='',
    license='Apache Software License',
    author='Kotaro Hara',
    tests_require=['pytest'],
    install_requires=['basemap>=1.0.7',
                      'matplotlib>=1.4.3',
                      'numpy>=1.9.2'],
    cmdclass={},
    author_email='koe.bluebear@gmail.com',
    description='Examples of geovisualizations using Python',
    long_description='',
    packages=['geovisualization'],
    include_package_data=True,
    platforms='any',
    test_suite='',
    classifiers=[],
    extra_require={}
)
from setuptools import setup, find_packages
import os

version = '0.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')
requires = [
    "formalchemy",
]

tests_require = [
    "pyramid",
]

setup(name='rebecca.form',
      version=version,
      description="pyramid view components based on formalchemy",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Atsushi Odagiri',
      author_email='aodagx@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='MIT',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['rebecca'],
      test_suite='rebecca.form',
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
        "testing": tests_require,
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

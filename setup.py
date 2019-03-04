#!/usr/bin/env python

from setuptools import setup, Command
import sys
import os.path
import subprocess
sys.path.insert(0, 'src')

version_py = os.path.join(os.path.dirname(__file__), 'src', 'SnmpLibrary',
                          'version.py')
try:
    version = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--dirty'],
            stderr=subprocess.STDOUT).rstrip().decode('ascii')
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (OSError, IOError, subprocess.CalledProcessError) as e:
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f.read(), d)
            version = d['__version__']
    except IOError:
        version = 'unknown'

with open('README.rst') as f:
        readme = f.read()


class run_build_libdoc(Command):
    description = "Build Robot Framework library documentation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            import robot.libdoc
        except ImportError:
            print("build_libdoc requires the Robot Framework package.")
            sys.exit(-1)

        robot.libdoc.libdoc('SnmpLibrary', 'docs/SnmpLibrary.html')


def main():
    setup(name='robotframework-snmplibrary',
          version=str(version),
          description='SNMP Library for Robot Framework',
          long_description=readme,
          author='Michael Walle',
          author_email='michael.walle@kontron.com',
          url='https://github.com/kontron/robotframework-snmplibrary',
          download_url='https://pypi.python.org/pypi/robotframework-snmplibrary',
          package_dir={'': 'src'},
          license='Apache License 2.0',
          classifiers=[
              'Development Status :: 4 - Beta',
              'Framework :: Robot Framework',
              'License :: OSI Approved :: Apache Software License',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Topic :: Software Development :: Testing',
          ],
          packages=['SnmpLibrary'],
          install_requires=['robotframework', 'pysnmp'],
          cmdclass={
              'build_libdoc': run_build_libdoc,
          },
    )


if __name__ == '__main__':
    main()

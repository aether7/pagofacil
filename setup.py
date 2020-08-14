import sys
from setuptools import setup

CURRENT_PYTHON_VERSION = sys.version_info[:2]
MINIMUM_PYTHON_VERSION = (3, 7)

if CURRENT_PYTHON_VERSION < MINIMUM_PYTHON_VERSION:
    sys.stderr.write("""
=====================================
Your python version is not supported
=====================================

this version of pago facil requires python {}.{}, however your
current version of python is {}.{}

This is because in this library we are using dataclasses lib.
""".format(*(MINIMUM_PYTHON_VERSION + CURRENT_PYTHON_VERSION)))
    sys.exit(1)

setup()

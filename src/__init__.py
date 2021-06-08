# -*- coding: utf-8 -*-

"""
dagpi.py
======================================
A synchronous python wrapper for Dagpi
"""

__author__ = "DJJ05"
__license__ = "MIT"
__title__ = "dagpi.py"
__version__ = '1.0.0'

from .client import Client
from .errors import WrapperException, DagpiException
from .reqs import ReqClient

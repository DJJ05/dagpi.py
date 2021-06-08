# -*- coding: utf-8 -*-

"""
client.py
======================================
Main client for interacting with Dagpi
"""
from typing import Optional

import requests

from .data import Data
from .reqs import ReqClient


class Client:
    """
    Main dagpi.py user client and interface

    Parameters
    ----------
    token
        String containing your dagpi token

    session (Optional)
        requests.Session to be used for making HTTP requests through the ReqClient
    """

    def __init__(self, token: str, session: Optional[requests.Session] = None) -> None:
        self.token = token
        self.session = session or requests.Session()
        self.reqs = ReqClient(token, self.session)
        self.data = Data(token, self.reqs)

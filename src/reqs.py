# -*- coding: utf-8 -*-

"""
reqs.py
=============================================
The request client for handling GETs to dagpi
"""

from typing import Optional

import requests

from .errors import DagpiException


class ReqClient():
    """
    Main class for handling requests with dagpi

    Parameters
    ----------
    authorization
        String containing dagpi token

    session
        Optional requests.session to use for requests
    """

    def __init__(self, authorization: str, session: Optional[requests.Session] = None) -> None:
        self.auth = authorization
        self.url = 'https://api.dagpi.xyz'
        self.user_agent = f'dagpi.py v1.0.0 {requests.utils.default_headers()["User-Agent"]}'
        self.session = session or requests.Session()
        self.headers = {
            'Authorization': self.auth,
            'User-Agent': self.user_agent
        }

    def data(self, endpoint: str) -> dict:
        """
        Sends a GET requests to a Dagpi data endpoint

        Parameters
        ----------
        endpoint
            String containing specific data endpoint

        Returns
        -------
        dict
        """
        url = f'{self.url}/data/{endpoint}'
        resp = self.session.get(url, headers=self.headers)
        if 300 >= resp.status_code >= 200 and resp.headers['Content-Type'] == 'application/json':
            return resp.json()
        raise DagpiException(resp.status_code)

    def image(self, endpoint: str, params: dict) -> tuple[str, bytes]:
        """
        Sends a GET requests to a Dagpi image endpoint

        Parameters
        ----------
        endpoint
            String containing specific data endpoint

        params
            Dict containing image parameters

        Returns
        -------
        tuple[str, bytes]
        """
        url = f'{self.url}/image/{endpoint}/'
        resp = self.session.get(url, headers=self.headers, params=params)
        if 300 >= resp.status_code >= 200 and resp.headers['Content-Type'].lower() in ('image/png', 'image/gif'):
            return resp.headers['Content-Type'].replace('image/', ''), resp.content
        raise DagpiException(resp.status_code)

# -*- coding: utf-8 -*-

"""
data.py
=================================
Class for handling data endpoints
"""

from .reqs import ReqClient


class Data:
    """
    Class for handling data endpoint functions

    Parameters
    ----------
    authorization
        String containing Dagpi token

    reqs
        reqs.ReqClient object for making requests
    """

    def __init__(self, authorization: str, reqs: ReqClient) -> None:
        self.authorization = authorization
        self.reqs = reqs

    def wtp(self) -> dict:
        """
        Who's that Pokemon

        Allows you to get a Dagpi WTP object
        """
        return self.reqs.data("wtp")

    def roast(self) -> dict:
        """
        Roast

        Allows you to get a roast
        """
        return self.reqs.data("roast")

    def joke(self) -> dict:
        """
        Joke

        Gets a nice edgy joke. Might be offensive/NSFW
        """
        return self.reqs.data("joke")

    def fact(self) -> dict:
        """
        Fact

        Gets a random fun fact
        """
        return self.reqs.data("fact")

    def eightball(self) -> dict:
        """
        8ball

        Gets a random 8ball response
        """
        return self.reqs.data("8ball")

    def yomama(self) -> dict:
        """
        Yomama

        Gets a nice yomama joke. Might be offensive/NSFW
        """
        return self.reqs.data("yomama")

    def waifu(self) -> dict:
        """
        Random Waifu

        Random Japanese Waifu
        """
        return self.reqs.data("waifu")

    def pickupline(self) -> dict:
        """
        Pickup Line

        Gets a pickup line. Might be offensive/NSFW
        """
        return self.reqs.data("pickupline")

    def headline(self) -> dict:
        """
        Headline

        Gets a headline. Can be either fake or real
        """
        return self.reqs.data("headline")

    def guessthelogo(self) -> dict:
        """
        Guess The Logo

        Random logo game. Gets logo JSON
        """
        return self.reqs.data("logo")

    def flag(self) -> dict:
        """
        Flag

        Gets random country flag and info
        """
        return self.reqs.data("flag")

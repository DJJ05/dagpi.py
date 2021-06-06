# -*- coding: utf-8 -*-

ERROR_MAP = {
    400: 'BAD REQUEST: Data inputted was incorrect or incorrectly formatted',
    401: 'UNAUTHORIZED: Token inputted was invalid and Dagpi couldn\'t authorize you',
    403: 'UNAUTHORIZED: Token inputted was invalid and Dagpi couldn\'t authorize you',
    408: 'REQUEST TIMEOUT: Connection with Dagpi is slow, and your request was unfulfilled',
    413: 'PAYLOAD TOO LARGE: Image / GIF inputted was too large (filesize) to process',
    415: 'UNSUPPORTED MEDIA: File extension is not support by Dagpi',
    422: 'UNPROCESSABLE: Dagpi couldn\'t manipulate the image you gave it',
    429: 'TOO MANY REQUESTS: Too many requests sent to Dagpi, you are being ratelimited',
    500: 'INTERNAL ERROR: Dagpi couldn\'t process the requests for unknown/undisclosed reasons'
}


class WrapperException(Exception):
    ...


class DagpiException(WrapperException):
    def __init__(self, code: int) -> None:
        self.code = code
        self.cause = ERROR_MAP.get(code, "UNKNOWN: Unknown Dagpi exception thrown")

    def __str__(self) -> str:
        return f'{self.code} | {self.cause}'

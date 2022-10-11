import json
from http.client import HTTPException as OriginalHTTPException
import requests


try:
    try:
        from config import settings
        DEFAULT_HEADERS = settings.DEFAULT_HEADERS
    except ModuleNotFoundError:
        from bds_framework.config import settings
        DEFAULT_HEADERS = settings.DEFAULT_HEADERS
except ModuleNotFoundError:
    DEFAULT_HEADERS = {}


class HTTPException(OriginalHTTPException):
    def __init__(self, message: str, url: str, status_code: object=None, reason: str=None, request_headers: dict=None, response_headers: dict=None):
        super().__init__(message)
        self.url = url
        self.status_code = status_code
        self.reason = reason
        self.request_headers = request_headers
        self.response_headers = response_headers
    

def get(url, headers={}, encoding='utf-8', decode=True, **kwargs):
    _headers = {**DEFAULT_HEADERS, **headers}
    response = requests.get(url, headers=_headers, **kwargs)

    if response.ok:
        byte_array_content = response.content
        return byte_array_content.decode(encoding) if decode and encoding is not None else byte_array_content
    else:
        raise HTTPException(f'{response.status_code} - {response.reason}', url, response.status_code, response.reason, _headers, response.headers)


def get_json(url, headers={}, encoding='utf-8', json_kwargs={}, **kwargs):
    content = get(url, headers=headers, encoding=encoding, **kwargs)
    return json.loads(content, **json_kwargs)

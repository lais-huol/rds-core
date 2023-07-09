from _typeshed import Incomplete
from http.client import HTTPException as OriginalHTTPException
from rds.core.config import settings as settings
from requests.structures import CaseInsensitiveDict
from typing import Any, Dict, List, Union

DEFAULT_HEADERS: Dict[str, Any]

class HTTPException(OriginalHTTPException):
    url: Incomplete
    status_code: Incomplete
    reason: Incomplete
    request_headers: Incomplete
    response_headers: Incomplete
    def __init__(
        self,
        message: str,
        url: str,
        status_code: Union[str, None] = ...,
        reason: Union[str, None] = ...,
        request_headers: Union[Dict[Any, Any], None] = ...,
        response_headers: Union[CaseInsensitiveDict, None] = ...,
    ) -> None: ...

def get(
    url: str,
    headers: Dict[str, str] = ...,
    encoding: str = ...,
    decode: bool = ...,
    **kwargs,
) -> Any: ...
def get_json(
    url: str,
    headers: Dict[str, str] = ...,
    encoding: str = ...,
    json_kwargs: Dict[str, Any] = ...,
    **kwargs,
) -> Union[List[Any], Dict[str, Any]]: ...

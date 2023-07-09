import datetime
from dynaconf.utils.boxing import DynaBox as DynaBox
from rds.core.config import settings as settings
from rds.core.helpers import instantiate_class as instantiate_class
from typing import Any, Dict, List, Union

def get_search_engine_config(alias: str = ...) -> DynaBox: ...
def search_engine(
    alias: str = ...,
    username: Union[str, None] = ...,
    password: Union[str, None] = ...,
): ...
def create_index_if_not_exists(
    index: str,
    body: Union[dict, None] = ...,
    params: Union[Dict[str, Any], None] = ...,
    headers: Union[Dict[str, Any], None] = ...,
    alias: str = ...,
) -> bool: ...
def delete_index_if_exists(
    index_name: str,
    params: Union[Dict[str, Any], None] = ...,
    headers: Union[Dict[str, Any], None] = ...,
    alias: str = ...,
    fail: bool = ...,
) -> bool: ...
def query(
    index_name: str,
    query_string: Union[str, int, float, datetime.date, datetime.datetime],
    fields: Union[List, None] = ...,
    alias: str = ...,
) -> Any: ...
def search(
    index_name: str,
    body: dict,
    alias: str = ...,
) -> Any: ...
def index(
    index_name: str,
    body: Union[dict, None] = ...,
    id: Any = ...,
    params: Union[Dict[str, Any], None] = ...,
    headers: Union[Dict[str, Any], None] = ...,
    alias: str = ...,
) -> Union[Any, Any]: ...
def search_engine_healthy(
    params: Union[Dict[str, Any], None] = ...,
    headers: Union[Dict[str, Any], None] = ...,
    alias: str = ...,
) -> bool: ...

from typing import Any, Dict, List

def get_class(full_class_name: str) -> Any: ...
def instantiate_class(
    full_class_name: str, *args: List, **kwargs: Dict[str, Any]
) -> Any: ...
def get_variable_by_pathname(full_class_name: str) -> Any: ...
def get_dict_by_pathname(obj: dict, ref: str) -> Any: ...

"""
Documentar.
"""
import logging

from typing import Any, List, Dict
import importlib


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_class(full_class_name: str) -> Any:
    module_name, class_name = full_class_name.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name)


def instantiate_class(
    full_class_name: str, *args: List, **kwargs: Dict[str, Any]
) -> Any:
    Klass = get_class(full_class_name)
    return Klass(*args, **kwargs)


def get_variable_by_pathname(full_class_name: str) -> Any:
    module_name, class_name = full_class_name.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name)


def get_dict_by_pathname(obj: dict, ref: str) -> Any:
    """
    Use MongoDB style 'something.by.dot' syntax to retrieve objects from Python dicts.

    Usage:
       >>> x = {"top": {"middle" : {"nested": "value"}}}
       >>> q = 'top.middle.nested'
       >>> get_dict_by_pathname(x,q)
       "value"

    Credit: https://gist.github.com/mittenchops/5664038
    """
    val = obj
    tmp = ref
    ref = tmp.replace(".XX", "[0]")
    if tmp != ref:
        logger.warning("Warning: replaced '.XX' with [0]-th index")
    for key in ref.split("."):
        idstart = key.find("[")
        embedslist = 1 if idstart > 0 else 0
        if embedslist:
            idx = int(key[idstart + 1 : key.find("]")])
            kyx = key[:idstart]
            try:
                val = val[kyx][idx]
            except IndexError:
                logger.warning(f"Index: x['{kyx}'][{idx}] does not exist.")
                raise
        else:
            val = val.get(key, None) if val is not None else None
    return val

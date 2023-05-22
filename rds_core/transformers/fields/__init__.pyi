from typing import Union, Dict, Any, List
from datetime import datetime

class Field:
    def __init__(self, source_field: Union[str, object, None]): ...
    def transform_to_dict(
        self,
        source_dict: Dict[str, Any],
        dest_dict: Dict[str, Any],
        dest_fieldname: str,
    ): ...
    def cast_source_value(self, source_value: Union[str, int, bool, float]): ...

class CharField(Field):
    pass

class DateField(Field):
    def __init__(self, source_field: str, format: str = "%d/%m/%Y"): ...
    def cast_source_value(
        self, source_value: Union[None, str, int, bool, float]
    ) -> datetime.date: ...

class DateTimeField(Field):
    def __init__(self, source_field: str, format: str = "%d/%m/%Y %H:%M:%S"): ...
    def cast_source_value(
        self, source_value: Union[str, int, bool, float]
    ) -> datetime: ...

class SimpleConcatField(Field):
    def __init__(self, fields: Union[List[str], None] = None, separator: str = ""): ...
    def transform_to_dict(
        self,
        source_dict: Dict[str, Any],
        dest_dict: Dict[str, Any],
        dest_fieldname: str,
    ) -> str: ...

class SubModelField(Field):
    def transform_to_dict(
        self,
        source_dict: Dict[str, Any],
        dest_dict: Dict[str, Any],
        dest_fieldname: str,
    ): ...

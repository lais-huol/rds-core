from typing import Union, Dict, Any

class ModelTransformer:
    __fields = None

    @classmethod
    def transform_to_dict(
        cls, source_dict: Union[Dict, None]
    ) -> Union[Dict[str, Any], None]: ...
    @classmethod
    def get_fields(cls) -> dict: ...

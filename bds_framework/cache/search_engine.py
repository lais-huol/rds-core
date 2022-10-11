from typing import Any

from bds_framework.cache.base import BaseCache, DEFAULT_TTL


class SearchEngineCache(BaseCache):
    def get(self, key: str, default: Any = None) -> Any:
        pass

    def set(self, key: str, value, ttl=DEFAULT_TTL) -> None:
        pass

    def touch(self, key: str, ttl=DEFAULT_TTL) -> bool:
        pass

    def delete(self, key: str) -> None:
        pass

    def clear(self) -> None:
        pass

    def add(self, key: str, value: Any, ttl: int = DEFAULT_TTL) -> bool:
        pass

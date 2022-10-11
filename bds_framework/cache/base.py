from typing import Any, List, Union
# from asgiref.sync import sync_to_async
# from django.utils.module_loading import import_string


UNDEFINED_TTL = object()
DEFAULT_TTL = 300


class BaseCache:
    _missing_key = object()

    def __init__(self, **params):
        self.default_ttl = int(params.get("ttl", DEFAULT_TTL))

    def get_ttl(self, ttl):
        return ttl if (isinstance(ttl, int) and ttl >= 0) or (ttl == UNDEFINED_TTL) else self.default_ttl

    def add(self, key: str, value: Any, ttl: int = UNDEFINED_TTL) -> bool:
        """ Define um valor no cache caso a chave ainda não exista.

            Caso já exista, não define o valor no cache, preservando o TTL.

            Args:
                key (_type_): A chave a ser usada para identificar o valor no cache.
                value (_type_): O valor a ser posto em cache.
                ttl (_type_, optional): O tempo máximo que o item pode existir no cache. O padrão é UNDEFINED_TTL.

            Raises:
                NotImplementedError: _description_

            Returns:
                bool: True adicionou, ou seja, se ainda não existia. False se já existia.
        """
        raise NotImplementedError("subclasses of BaseCache must provide an add() method")

    def get(self, key: str, default: Any = None) -> Any:
        """ Busca uma determinada chave no cache. Se a chave não existir, retorne o padrão, que por padrão é None.
            Args:
                key (_type_): A chave a ser usada para identificar o valor no cache.
                default (_type_): O valor padrão, caso não seja encontrado no cache. O padrão é None.
            Raises:
                NotImplementedError: _description_
        """
        raise NotImplementedError("subclasses of BaseCache must provide a get() method")

    def set(self, key: str, value: Any, ttl: int = UNDEFINED_TTL) -> None:
        """ Set a value in the cache. If ttl is given, use that ttl for the key; otherwise use the default cache ttl.
        """
        raise NotImplementedError("subclasses of BaseCache must provide a set() method")

    def delete(self, key: str) -> None:
        """ Delete a key from the cache and return whether it succeeded, failing silently.
        """
        raise NotImplementedError("subclasses of BaseCache must provide a delete() method")

    # def touch(self, key: str, ttl: int = UNDEFINED_TTL) -> bool:
    #     """
    #         Update the key's expiry time using ttl. Return True if successful or False if the key does not exist.
    #     """
    #     raise NotImplementedError("subclasses of BaseCache must provide a touch() method")
    #
    # def get_many(self, keys: List[str]) -> List[Any]:
    #     """
    #         Fetch a bunch of keys from the cache. For certain backends (memcached, pgsql) this can be *much* faster when fetching multiple values.
    #
    #         Return a dict mapping each key in keys to its value. If the given key is missing, it will be missing from the response dict.
    #     """
    #     d = {}
    #     for k in keys:
    #         val = self.get(k, self._missing_key)
    #         if val is not self._missing_key:
    #             d[k] = val
    #     return d
    #
    # def get_or_set(self, key: str, default: Any, ttl: int = UNDEFINED_TTL) -> Any:
    #     """ Fetch a given key from the cache. If the key does not exist,
    #         add the key and set it to the default value. The default value can
    #         also be any callable. If ttl is given, use that ttl for the
    #         key; otherwise use the default cache ttl.
    #
    #         Return the value of the key stored or retrieved.
    #     """
    #     val = self.get(key, self._missing_key)
    #     if val is self._missing_key:
    #         if callable(default):
    #             default = default()
    #         self.add(key, default, ttl=ttl)
    #         # Fetch the value again to avoid a race condition if another caller
    #         # added a value between the first get() and the add() above.
    #         return self.get(key, default)
    #     return val
    #
    # def has_key(self, key: str) -> bool:
    #     """ Return True if the key is in the cache and has not expired. """
    #     return (
    #         self.get(key, self._missing_key) is not self._missing_key
    #     )
    #
    # def incr(self, key: str, delta: int = 1) -> Union[int, float]:
    #     """ Add delta to value in the cache. If the key does not exist, raise a ValueError exception. """
    #     value = self.get(key, self._missing_key)
    #     if value is self._missing_key:
    #         raise ValueError("Key '%s' not found" % key)
    #     new_value = value + delta
    #     self.set(key, new_value)
    #     return new_value
    #
    # def decr(self, key: str, delta: int = 1) -> Union[int, float]:
    #     """ Subtract delta from value in the cache. If the key does not exist, raise a ValueError exception.
    #     """
    #     return self.incr(key, -delta)
    #
    # def __contains__(self, key: Any) -> bool:
    #     """ Return True if the key is in the cache and has not expired. """
    #     # This is a separate method, rather than just a copy of has_key(),
    #     # so that it always has the same functionality as has_key(), even
    #     # if a subclass overrides it.
    #     return self.has_key(key)
    #
    # def set_many(self, data: Any, ttl: int = UNDEFINED_TTL) -> List[Any]:
    #     """ Set a bunch of values in the cache at once from a dict of key/value
    #         pairs.  For certain backends (memcached), this is much more efficient
    #         than calling set() multiple times.
    #
    #         If ttl is given, use that ttl for the key; otherwise use the
    #         default cache ttl.
    #
    #         On backends that support it, return a list of keys that failed
    #         insertion, or an empty list if all keys were inserted successfully.
    #     """
    #     for key, value in data.items():
    #         # self.set(key, value, ttl=ttl)
    #         self.set(key, value, ttl=ttl)
    #     return []
    #
    # def delete_many(self, keys: List[str]) -> None:
    #     """ Delete a bunch of values in the cache at once. For certain backends
    #         (memcached), this is much more efficient than calling delete() multiple times.
    #     """
    #     for key in keys:
    #         self.delete(key)
    #
    # def clear(self) -> None:
    #     """ Remove *all* values from the cache at once. """
    #     raise NotImplementedError("subclasses of BaseCache must provide a clear() method")
    #
    # def close(self, **kwargs) -> None:
    #     """ Close the cache connection """
    #     pass

from typing import Any

from bds_framework.cache.base import BaseCache, UNDEFINED_TTL
from bds_framework.searchengine import search_engine as search_engine_func


class SearchEngineCache(BaseCache):

    def __init__(self, **params):
        super(SearchEngineCache, self).__init__(**params)
        self.search_engine_alias = params.get("search_engine_alias", 'default')
        self.index_name = params.get("index_name", 'cnes_establecimento_cache')

    @property
    def search_engine(self):
        return search_engine_func(self.search_engine_alias)

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
        if self.search_engine.exists(self.index_name, id=key):
            return False
        self.search_engine.create(self.index_name, body={'value': value, 'ttl': 1}, id=key)
        return True

    def get(self, key: str, default: Any = None) -> Any:
        doc = self.search_engine.get(self.index_name, key)['_source']
        ttl = doc['ttl']
        return doc['value']

    def set(self, key: str, value: Any, ttl: int = UNDEFINED_TTL) -> None:
        self.search_engine.index(self.index_name, body={'value': value, 'ttl': 1}, id=key)

    def delete(self, key: str) -> None:
        self.search_engine.delete(self.index_name, id=key)

    def touch(self, key: str, ttl: int = UNDEFINED_TTL) -> bool:
        pass

    def clear(self) -> None:
        pass
        # self.search_engine.delete_by_query(
        #     self.index_name,
        #     body={
        #         'size': 5,
        #         'query': {
        #             'multi_match': {
        #                 'query': '',
        #             }
        #         }
        #     }
        # )

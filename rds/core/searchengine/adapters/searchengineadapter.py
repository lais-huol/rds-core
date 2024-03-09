# -*- coding: utf-8 -*-
from typing import Any, Self
from datetime import datetime, date
from abc import ABC, abstractmethod


class ToManyHits(Exception):
    pass


class CatClient:
    pass


class ClusterClient:
    pass


class DanglingIndicesClient:
    pass


class IndicesClient:
    pass


class IngestClient:
    pass


class NodesClient:
    pass


class NodesClient:
    pass


class RemoteClient:
    pass


class SecurityClient:
    pass


class SnapshotClient:
    pass


class TasksClient:
    pass


class RemoteStoreClient:
    pass


class FeaturesClient:
    pass


class PluginsClient:
    pass


class HttpClient:
    pass


class SearchEngineAdapter(ABC):

    def __init__(self, clustername: str | None = "default", **kwargs: Any) -> None:
        self._clusternamet: str = clustername
        self._wrapped: Any = None
        self._cat: CatClient = None
        self._cluster: ClusterClient = None
        self._dangling_indices: DanglingIndicesClient = None
        self._indices: IndicesClient = None
        self._ingest: IngestClient = None
        self._nodes: NodesClient = None
        self._remote: RemoteClient = None
        self._security: SecurityClient = None
        self._snapshot: SnapshotClient = None
        self._tasks: TasksClient = None
        self._remote_store: RemoteStoreClient = None
        self._features: FeaturesClient = None
        self._plugins: PluginsClient = None
        self._http: HttpClient = None

    @property
    def transport(self) -> Any:
        return self._wrapped.transport

    @property
    def cat(self) -> CatClient:
        return self._cat

    @property
    def cluster(self) -> ClusterClient:
        return self._cluster

    @property
    def dangling_indices(self) -> DanglingIndicesClient:
        return self._dangling_indices

    @property
    def indices(self) -> IndicesClient:
        return self._indices

    @property
    def ingest(self) -> IngestClient:
        return self._ingest

    @property
    def nodes(self) -> NodesClient:
        return self._nodes

    @property
    def nodes(self) -> NodesClient:
        return self._nodes

    @property
    def remote(self) -> RemoteClient:
        return self._remote

    @property
    def security(self) -> SecurityClient:
        return self._security

    @property
    def snapshot(self) -> SnapshotClient:
        return self._snapshot

    @property
    def tasks(self) -> TasksClient:
        return self._tasks

    @property
    def remote_store(self) -> RemoteStoreClient:
        return self._remote_store

    @property
    def features(self) -> FeaturesClient:
        return self._features

    @property
    def plugins(self) -> PluginsClient:
        return self._plugins

    @property
    def http(self) -> HttpClient:
        return self._http

    @abstractmethod
    def __repr__(self) -> Any: ...

    @abstractmethod
    def __enter__(self) -> Any: ...

    @abstractmethod
    def __exit__(self, *_: Any) -> None: ...

    @abstractmethod
    def close(self) -> None: ...

    @abstractmethod
    def ping(self, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def info(self, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def create(self, index: Any, id: Any, body: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def index(self, index: Any, body: Any, id: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def bulk(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def clear_scroll(self, body: Any = None, scroll_id: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def count(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete_by_query(self, index: Any, body: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete_by_query_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete_script(self, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def exists(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def exists_source(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def explain(self, index: Any, id: Any, body: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def field_caps(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get_script(self, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get_source(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def mget(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def msearch(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def msearch_template(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def mtermvectors(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def put_script(self, id: Any, body: Any, context: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def rank_eval(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def reindex(self, body: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def reindex_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def render_search_template(
        self, body: Any = None, id: Any = None, params: Any = None, headers: Any = None
    ) -> Any: ...

    @abstractmethod
    def scripts_painless_execute(self, body: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def scroll(self, body: Any = None, scroll_id: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def search(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def search_shards(self, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def search_template(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def termvectors(
        self, index: Any, body: Any = None, id: Any = None, params: Any = None, headers: Any = None
    ) -> Any: ...

    @abstractmethod
    def update(self, index: Any, id: Any, body: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def update_by_query(self, index: Any, body: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def update_by_query_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get_script_context(self, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get_script_languages(self, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def create_pit(self, index: Any, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete_all_pits(self, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def delete_pit(self, body: Any = None, params: Any = None, headers: Any = None) -> Any: ...

    @abstractmethod
    def get_all_pits(self, params: Any = None, headers: Any = None) -> Any: ...

    def proxy(self, username: str, password: str) -> Self:
        pass

    def create_index(
        self, index: str, body: dict | None = None, params: dict | None = None, headers: dict | None = None
    ) -> bool:
        """
        Cria um índice caso não exista. Retorna True se criou e False se não criou.

        Args:
            index (str): nome do índice a ser criado
            body (dict|None): corpo do índice
            params (dict|None): parametros
            headers (dict|None): cabeçalhos

        Raises:
            exception: Erro conforme retornado pelo Search Engine.

        Returns:
            bool: True se criou. False se não criou.
        """
        try:
            self.indices.create(index, body=body or {}, params=params, headers=headers)  # type: ignore
            return True
        except Exception as e:
            if getattr(e, "error", None) == "resource_already_exists_exception":
                return False
            raise e

    def delete_index(self, index_name: str, params: dict | None = None, headers: dict | None = None) -> bool:
        """
        Apaga um índice caso exista. Retorna True se apagou e False se não apagou.

        Args:
            index_name (str): nome do índice a ser criado
            params (Dict[str, Any] | None):
            headers (Dict[str, Any] | None): Union[Dict[str, Any], None] = None,
            alias (str): alias para o search engine

        Raises:
            Exception: Erro conforme retornado pelo Search Engine.

        Returns:
            bool: True se criou. False se não criou.
        """
        try:
            self.indices.delete(index_name, params=params, headers=headers)  # type: ignore
            return True
        except Exception as e:
            if getattr(e, "error", None) == "index_not_found_exception":
                return False
            raise Exception(e)

    def get_by_term(
        self, index_name: str, term: str, term_value: str | int | float | date | datetime, fields: list | None = None
    ) -> Any | None:
        if fields is None:
            fields = []
        response = self.search(index=index_name, body={"query": {"term": {term: term_value}}})
        if response["hits"]["total"]["value"] > 1:
            raise ToManyHits()
        if response["hits"]["total"]["value"] == 0:
            return None
        return response["hits"]["hits"][0]["_source"]

    def healthy(self) -> bool:
        try:
            self.ping()
            return True
        except:
            return False

# -*- coding: utf-8 -*-
from typing import Any, Self, Callable
from datetime import datetime, date
from abc import ABC, abstractmethod
from functools import wraps


GLOBAL_PARAMS = ("pretty", "human", "error_trace", "format", "filter_path")
string_types = str, bytes


def _escape(value: Any) -> Any:
    """
    Escape a single value of a URL string or a query parameter. If it is a list
    or tuple, turn it into a comma-separated string first.
    """

    # make sequences into comma-separated stings
    if isinstance(value, (list, tuple)):
        value = ",".join(value)

    # dates and datetimes into isoformat
    elif isinstance(value, (date, datetime)):
        value = value.isoformat()

    # make bools into true/false strings
    elif isinstance(value, bool):
        value = str(value).lower()

    # don't decode bytestrings
    elif isinstance(value, bytes):
        return value

    # encode strings to utf-8
    if isinstance(value, string_types):
        if isinstance(value, str):
            return value.encode("utf-8")

    return str(value)


def query_params(*opensearch_query_params: Any) -> Callable:  # type: ignore
    """
    Decorator that pops all accepted parameters from method's kwargs and puts
    them in the params argument.
    """

    def _wrapper(func: Any) -> Any:
        @wraps(func)
        def _wrapped(*args: Any, **kwargs: Any) -> Any:
            params = (kwargs.pop("params", None) or {}).copy()
            headers = {k.lower(): v for k, v in (kwargs.pop("headers", None) or {}).copy().items()}

            if "opaque_id" in kwargs:
                headers["x-opaque-id"] = kwargs.pop("opaque_id")

            http_auth = kwargs.pop("http_auth", None)
            api_key = kwargs.pop("api_key", None)

            if http_auth is not None and api_key is not None:
                raise ValueError("Only one of 'http_auth' and 'api_key' may be passed at a time")
            elif http_auth is not None:
                headers["authorization"] = "Basic %s" % (_base64_auth_header(http_auth),)
            elif api_key is not None:
                headers["authorization"] = "ApiKey %s" % (_base64_auth_header(api_key),)

            # don't escape ignore, request_timeout, or timeout
            for p in ("ignore", "request_timeout", "timeout"):
                if p in kwargs:
                    params[p] = kwargs.pop(p)

            for p in opensearch_query_params + GLOBAL_PARAMS:
                if p in kwargs:
                    v = kwargs.pop(p)
                    if v is not None:
                        params[p] = _escape(v)

            return func(*args, params=params, headers=headers, **kwargs)

        return _wrapped

    return _wrapper


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

    def __repr__(self) -> Any:
        return self._wrapped.__repr__()

    def __enter__(self) -> Any:
        return self._wrapped.__enter__()

    def __exit__(self, *_: Any) -> None:
        self._wrapped.__exit__(_)

    def close(self) -> None:
        self._wrapped.close()

    @query_params()
    def ping(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.ping(params=params, headers=headers)

    @query_params()
    def info(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.info(params=params, headers=headers)

    @query_params("pipeline", "refresh", "routing", "timeout", "version", "version_type", "wait_for_active_shards")
    def create(self, index: Any, id: Any, body: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.create(index=index, id=id, body=body, params=params, headers=headers)

    @query_params(
        "if_primary_term",
        "if_seq_no",
        "op_type",
        "pipeline",
        "refresh",
        "require_alias",
        "routing",
        "timeout",
        "version",
        "version_type",
        "wait_for_active_shards",
    )
    def index(self, index: Any, body: Any, id: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.index(index=index, body=body, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "pipeline",
        "refresh",
        "require_alias",
        "routing",
        "timeout",
        "wait_for_active_shards",
    )
    def bulk(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.bulk(body=body, index=index, params=params, headers=headers)

    @query_params()
    def clear_scroll(self, body: Any = None, scroll_id: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.clear_scroll(body=body, scroll_id=scroll_id, params=params, headers=headers)

    @query_params(
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "expand_wildcards",
        "ignore_throttled",
        "ignore_unavailable",
        "lenient",
        "min_score",
        "preference",
        "q",
        "routing",
        "terminate_after",
    )
    def count(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.count(body=body, index=index, params=params, headers=headers)

    @query_params(
        "if_primary_term",
        "if_seq_no",
        "refresh",
        "routing",
        "timeout",
        "version",
        "version_type",
        "wait_for_active_shards",
    )
    def delete(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete(index=index, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "conflicts",
        "default_operator",
        "df",
        "expand_wildcards",
        "from_",
        "ignore_unavailable",
        "lenient",
        "max_docs",
        "preference",
        "q",
        "refresh",
        "request_cache",
        "requests_per_second",
        "routing",
        "scroll",
        "scroll_size",
        "search_timeout",
        "search_type",
        "size",
        "slices",
        "sort",
        "stats",
        "terminate_after",
        "timeout",
        "version",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def delete_by_query(self, index: Any, body: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete_by_query(index=index, body=body, params=params, headers=headers)

    @query_params("requests_per_second")
    def delete_by_query_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete_by_query_rethrottle(task_id=task_id, params=params, headers=headers)

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def delete_script(self, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete_script(id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
        "version",
        "version_type",
    )
    def exists(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.exists(index=index, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "version",
        "version_type",
    )
    def exists_source(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.exists_source(index=index, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "analyze_wildcard",
        "analyzer",
        "default_operator",
        "df",
        "lenient",
        "preference",
        "q",
        "routing",
        "stored_fields",
    )
    def explain(self, index: Any, id: Any, body: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.explain(index=index, id=id, body=body, params=params, headers=headers)

    @query_params("allow_no_indices", "expand_wildcards", "fields", "ignore_unavailable", "include_unmapped")
    def field_caps(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.field_caps(body=body, index=index, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
        "version",
        "version_type",
    )
    def get(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get(index=index, id=id, params=params, headers=headers)

    @query_params("cluster_manager_timeout", "master_timeout")
    def get_script(self, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get_script(id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "version",
        "version_type",
    )
    def get_source(self, index: Any, id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get_source(index=index, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "preference",
        "realtime",
        "refresh",
        "routing",
        "stored_fields",
    )
    def mget(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.mget(body=body, index=index, params=params, headers=headers)

    @query_params(
        "ccs_minimize_roundtrips",
        "max_concurrent_searches",
        "max_concurrent_shard_requests",
        "pre_filter_shard_size",
        "rest_total_hits_as_int",
        "search_type",
        "typed_keys",
    )
    def msearch(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.msearch(body=body, index=index, params=params, headers=headers)

    @query_params(
        "ccs_minimize_roundtrips", "max_concurrent_searches", "rest_total_hits_as_int", "search_type", "typed_keys"
    )
    def msearch_template(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.msearch_template(body=body, index=index, params=params, headers=headers)

    @query_params(
        "field_statistics",
        "fields",
        "ids",
        "offsets",
        "payloads",
        "positions",
        "preference",
        "realtime",
        "routing",
        "term_statistics",
        "version",
        "version_type",
    )
    def mtermvectors(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.mtermvectors(body=body, index=index, params=params, headers=headers)

    @query_params("cluster_manager_timeout", "master_timeout", "timeout")
    def put_script(self, id: Any, body: Any, context: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.put_script(id=id, body=body, context=context, params=params, headers=headers)

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "search_type")
    def rank_eval(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.rank_eval(body=body, index=index, params=params, headers=headers)

    @query_params(
        "max_docs",
        "refresh",
        "requests_per_second",
        "scroll",
        "slices",
        "timeout",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def reindex(self, body: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.reindex(body=body, params=params, headers=headers)

    @query_params("requests_per_second")
    def reindex_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.reindex_rethrottle(task_id=task_id, params=params, headers=headers)

    @query_params()
    def render_search_template(self, body: Any = None, id: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.render_search_template(body=body, id=id, params=params, headers=headers)

    @query_params()
    def scripts_painless_execute(self, body: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.scripts_painless_execute(body=body, params=params, headers=headers)

    @query_params("rest_total_hits_as_int", "scroll")
    def scroll(self, body: Any = None, scroll_id: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.scroll(body=body, scroll_id=scroll_id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "allow_partial_search_results",
        "analyze_wildcard",
        "analyzer",
        "batched_reduce_size",
        "ccs_minimize_roundtrips",
        "default_operator",
        "df",
        "docvalue_fields",
        "expand_wildcards",
        "explain",
        "from_",
        "ignore_throttled",
        "ignore_unavailable",
        "lenient",
        "max_concurrent_shard_requests",
        "pre_filter_shard_size",
        "preference",
        "q",
        "request_cache",
        "rest_total_hits_as_int",
        "routing",
        "scroll",
        "search_type",
        "seq_no_primary_term",
        "size",
        "sort",
        "stats",
        "stored_fields",
        "suggest_field",
        "suggest_mode",
        "suggest_size",
        "suggest_text",
        "terminate_after",
        "timeout",
        "track_scores",
        "track_total_hits",
        "typed_keys",
        "version",
    )
    def search(self, body: Any = None, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.search(body=body, index=index, params=params, headers=headers)

    @query_params("allow_no_indices", "expand_wildcards", "ignore_unavailable", "local", "preference", "routing")
    def search_shards(self, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.search_shards(index=index, params=params, headers=headers)

    @query_params(
        "allow_no_indices",
        "ccs_minimize_roundtrips",
        "expand_wildcards",
        "explain",
        "ignore_throttled",
        "ignore_unavailable",
        "preference",
        "profile",
        "rest_total_hits_as_int",
        "routing",
        "scroll",
        "search_type",
        "typed_keys",
    )
    def search_template(self, body: Any, index: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.search_template(body=body, index=index, params=params, headers=headers)

    @query_params(
        "field_statistics",
        "fields",
        "offsets",
        "payloads",
        "positions",
        "preference",
        "realtime",
        "routing",
        "term_statistics",
        "version",
        "version_type",
    )
    def termvectors(self, index: Any, body: Any = None, id: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.termvectors(index=index, body=body, id=id, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "if_primary_term",
        "if_seq_no",
        "lang",
        "refresh",
        "require_alias",
        "retry_on_conflict",
        "routing",
        "timeout",
        "wait_for_active_shards",
    )
    def update(self, index: Any, id: Any, body: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.update(index=index, id=id, body=body, params=params, headers=headers)

    @query_params(
        "_source",
        "_source_excludes",
        "_source_includes",
        "allow_no_indices",
        "analyze_wildcard",
        "analyzer",
        "conflicts",
        "default_operator",
        "df",
        "expand_wildcards",
        "from_",
        "ignore_unavailable",
        "lenient",
        "max_docs",
        "pipeline",
        "preference",
        "q",
        "refresh",
        "request_cache",
        "requests_per_second",
        "routing",
        "scroll",
        "scroll_size",
        "search_timeout",
        "search_type",
        "size",
        "slices",
        "sort",
        "stats",
        "terminate_after",
        "timeout",
        "version",
        "wait_for_active_shards",
        "wait_for_completion",
    )
    def update_by_query(self, index: Any, body: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.update_by_query(index=index, body=body, params=params, headers=headers)

    @query_params("requests_per_second")
    def update_by_query_rethrottle(self, task_id: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.update_by_query_rethrottle(task_id=task_id, params=params, headers=headers)

    @query_params()
    def get_script_context(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get_script_context(params=params, headers=headers)

    @query_params()
    def get_script_languages(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get_script_languages(params=params, headers=headers)

    @query_params("allow_partial_pit_creation", "expand_wildcards", "keep_alive", "preference", "routing")
    def create_pit(self, index: Any, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.create_pit(index=index, params=params, headers=headers)

    @query_params()
    def delete_all_pits(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete_all_pits(params=params, headers=headers)

    @query_params()
    def delete_pit(self, body: Any = None, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.delete_pit(body=body, params=params, headers=headers)

    @query_params()
    def get_all_pits(self, params: Any = None, headers: Any = None) -> Any:
        return self._wrapped.get_all_pits(params=params, headers=headers)

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
        self,
        index_name: str,
        term: str,
        term_value: str | int | float | date | datetime,
        fields: list[str] | None = None,
    ) -> dict | None:
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

import datetime
from typing import Dict, Union, Any, List
from dynaconf.utils.boxing import DynaBox
from opensearchpy import OpenSearch
from opensearchpy.client import (
    CatClient,
    ClusterClient,
    DanglingIndicesClient,
    IndicesClient,
    IngestClient,
    NodesClient,
    RemoteClient,
    SecurityClient,
    SnapshotClient,
    TasksClient,
    RemoteStoreClient,
    FeaturesClient,
    PluginsClient,
    HttpClient,
)
from opensearchpy.client.utils import query_params
from rds.core.config import settings
from rds.core.helpers import instantiate_class
from rds.core.searchengine.adapters.searchengineadapter import SearchEngineAdapter


class OpenSearchAdapter(SearchEngineAdapter):
    def __init__(self, clustername: str | None = "default", **kwargs: Any) -> None:
        """
        :arg cluster_alias: alias for list of nodes, or a single node, we should connect to.
        :arg kwargs: any additional arguments will be passed on to the
            :class:`~opensearchpy.Transport` class and, subsequently, to the
            :class:`~opensearchpy.Connection` instances.
        """
        super().__init__(clustername, **kwargs)
        self._wrapped = OpenSearch(hosts=settings.SEARCH_ENGINES.get(clustername, {}).get("hosts", None), **kwargs)

    @property
    def cat(self) -> CatClient:
        if self._cat is None:
            self._cat = CatClient(self)
        return self._cat

    @property
    def cluster(self) -> ClusterClient:
        if self._cluster is None:
            self._cluster = ClusterClient(self)
        return self._cluster

    @property
    def dangling_indices(self) -> DanglingIndicesClient:
        if self._dangling_indices is None:
            self._dangling_indices = DanglingIndicesClient(self)
        return self._dangling_indices

    @property
    def indices(self) -> IndicesClient:
        if self._indices is None:
            self._indices = IndicesClient(self)
        return self._indices

    @property
    def ingest(self) -> IngestClient:
        if self._ingest is None:
            self._ingest = IngestClient(self)
        return self._ingest

    @property
    def nodes(self) -> NodesClient:
        if self._nodes is None:
            self._nodes = NodesClient(self)
        return self._nodes

    @property
    def nodes(self) -> NodesClient:
        if self._nodes is None:
            self._nodes = NodesClient(self)
        return self._nodes

    @property
    def remote(self) -> RemoteClient:
        if self._remote is None:
            self._remote = RemoteClient(self)
        return self._remote

    @property
    def security(self) -> SecurityClient:
        if self._security is None:
            self._security = SecurityClient(self)
        return self._security

    @property
    def snapshot(self) -> SnapshotClient:
        if self._snapshot is None:
            self._snapshot = SnapshotClient(self)
        return self._snapshot

    @property
    def tasks(self) -> TasksClient:
        if self._tasks is None:
            self._tasks = TasksClient(self)
        return self._tasks

    @property
    def remote_store(self) -> RemoteStoreClient:
        if self._remote_store is None:
            self._remote_store = RemoteStoreClient(self)
        return self._remote_store

    @property
    def features(self) -> FeaturesClient:
        if self._features is None:
            self._features = FeaturesClient(self)
        return self._features

    @property
    def plugins(self) -> PluginsClient:
        if self._plugins is None:
            self._features = PluginsClient(self)
        return self._plugins

    @property
    def http(self) -> HttpClient:
        if self._http is None:
            self._http = HttpClient(self)
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

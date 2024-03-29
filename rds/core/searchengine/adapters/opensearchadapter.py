from typing import Any
from opensearchpy import OpenSearch, Search
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
from rds.core.searchengine import get_searchengine_config
from rds.core.searchengine.adapters.searchengineadapter import SearchEngineAdapter, query_params


class OpenSearchAdapter(SearchEngineAdapter):
    def __init__(self, clustername: str | None = "default", **kwargs: Any) -> None:
        """
        :arg cluster_alias: alias for list of nodes, or a single node, we should connect to.
        :arg kwargs: any additional arguments will be passed on to the
            :class:`~opensearchpy.Transport` class and, subsequently, to the
            :class:`~opensearchpy.Connection` instances.
        """
        super().__init__(clustername, **kwargs)

        config = get_searchengine_config(clustername)
        self._wrapped = OpenSearch(hosts=config.get("hosts", None), **kwargs)

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
        return Search(using=self._wrapped, index=index)

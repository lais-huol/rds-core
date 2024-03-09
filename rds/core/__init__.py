# -*- coding: utf-8 -*-
"""
RDS é **acrônimo** para Rede de Dados em Saúde. Este framework/api condensa um conjunto de boas práticas para o
desenvolvimento das aplicações que compõem ou comporão a RDS do LAIS e dos parceiros que contratarem o LAIS para fazer
suas próprias RDS, a exemplo REDS-RN e RDS-ES.
"""
from typing import Optional, Union, Any, List
from enum import Enum
from requests import get as original_get, auth
from rds.core.config import settings
from rds.core.searchengine import searchengines, ToManyHits, RDS_HOSTS
from opensearchpy import Search


class TEMPERATURE:
    COLD = "COLD"
    WARN = "WARN"
    HOT = "HOT"


def cold(source):
    source["@temperature"] = TEMPERATURE.COLD
    return source


def warn_hot(source):
    source["@temperature"] = TEMPERATURE.WARN if source.get("@cached", False) else TEMPERATURE.HOT
    return source


class Service:

    def __init__(self) -> None:
        self._url_prefix = None

    def __get(self, url_suffix: str) -> dict:
        if self._url_prefix is None:
            raise ValueError("Informe o __url_prefix no construtor da classe.")
        response = original_get(self._url_prefix + url_suffix)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    @property
    def is_up(self) -> bool:
        return self.__get("/healthz/").get("status") == "ok"

    @property
    def health(self) -> dict:
        return self.__get("/health/")


class Resource:

    def __init__(self, cluster: str = "default") -> None:
        self._searchengine = None
        self._cluster = "default"
        self._index_name = None

    @property
    def cluster(self) -> str:
        if self._cluster is None:
            raise ValueError("Informe o índice no construtor da classe.")
        return self._cluster

    @property
    def index_name(self) -> str:
        if self._index_name is None:
            raise ValueError("Informe o índice no construtor da classe.")
        return self._index_name

    @property
    def searchengine(self):
        if self._searchengine is None:
            self._searchengine = searchengines(self.cluster)
        return self._searchengine

    @property
    def info(self):
        data = self._get(f"{RDS_HOSTS}/{self.index_name}/")
        root = list(data.keys())[0]
        return data[root]

    @property
    def mappings(self):
        return self.info.get("mappings")

    @property
    def settings(self):
        return self.info.get("settings")

    @property
    def aliases(self):
        return self.info.get("aliases")

    @property
    def search(self):
        return Search(using=self.se, index=self.index_name)

    def query(self, query: dict, filter_path: Optional[List[str]] = None, *args, **kwargs) -> dict:
        return self.searchengine.search(
            index=self.index_name, body={"query": query}, filter_path=filter_path, *args, **kwargs
        )

    def _get(self, url: str) -> dict:
        basic = auth.HTTPBasicAuth(**dict(settings.get("RDS")))
        response = original_get(url, auth=basic)
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

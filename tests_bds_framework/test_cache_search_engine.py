import unittest
import pytest
from bds_framework.cache import caches
from bds_framework.searchengine import create_index_if_not_exists, delete_index_if_exists
from tests_bds_framework.cache_mixin import CacheMixin


class TestSearchEngineCache(CacheMixin, unittest.TestCase):

    def __init__(self, method_name: str = 'runTest') -> None:
        super(TestSearchEngineCache, self).__init__(method_name)
        self.test_index = 'test_index_cache'
        self.cache = caches['search_engine']
        self.cache_name = 'search_engine'

    def setUp(self):
        delete_index_if_exists(self.test_index)
        create_index_if_not_exists(self.test_index)
        super().setUp()

    def tearDown(self):
        delete_index_if_exists(self.test_index)

    def test_clear(self):
        with pytest.raises(Exception):
            self.cache.clear()

    def test_binary_string(self):
        from zlib import compress
        with self.assertRaises(ValueError):
            self.cache.set('key', compress("value_to_be_compressed".encode()))

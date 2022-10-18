import time
import unittest
import pytest
from bds_framework.cache import caches
from bds_framework.searchengine import create_index_if_not_exists, delete_index_if_exists
from tests_bds_framework.test_cache_mixin import TestCacheMixin
# from elasticmock import elasticmock


class TestSearchEngineCache(TestCacheMixin, unittest.TestCase):

    def __init__(self, methodName: str = 'runTest'):
        super(TestSearchEngineCache, self).__init__(methodName)
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

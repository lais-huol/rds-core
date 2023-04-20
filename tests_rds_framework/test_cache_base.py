import unittest
import pytest
from rds_framework.cache.base import BaseCache


class TestBaseCase(unittest.TestCase):

    def __init__(self, method_nname: str = 'runTest'):
        self.cache = BaseCache()
        super().__init__(methodName=method_nname)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_cache_class(self):
        self.assertIsInstance(self.cache, BaseCache)

    def test_add(self):
        with pytest.raises(NotImplementedError):
            self.cache.add("test_add", "value")

    def test_get(self):
        with pytest.raises(NotImplementedError):
            self.cache.get("test_add")

    def test_set(self):
        with pytest.raises(NotImplementedError):
            self.cache.set("test_add", "value")

    def test_delete(self):
        with pytest.raises(NotImplementedError):
            self.cache.delete("test_add")

    def test_touch(self):
        with pytest.raises(NotImplementedError):
            self.cache.touch("test_add")

    def test_clear(self):
        with pytest.raises(NotImplementedError):
            self.cache.clear()

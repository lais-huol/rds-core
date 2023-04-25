import datetime
import unittest
from rds_core.cache import caches


class NoCacheTests(unittest.TestCase):

    def __init__(self, methodName: str = 'runTest'):
        super(NoCacheTests, self).__init__(methodName)
        self.cache_name = 'default'
        self.cache = caches[self.cache_name]

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().setUp()

    def test_add(self):
        self.assertTrue(self.cache.add("addkey1", "value"))

    def test_key_exists(self):
        self.assertTrue(self.cache.add("test_has_key", 'value'))
        self.assertFalse(self.cache.key_exists("test_has_key"))

    def test_get(self):
        self.assertTrue(self.cache.add("test_get", "value1"))
        self.assertIsNone(self.cache.get("test_get"), 'value1')

    def test_set(self):
        self.assertIsNone(self.cache.set("test_set", "value1"))
        self.assertIsNone(self.cache.get("test_set"), 'value1')

    def test_get_or_set(self):
        self.assertIsNone(self.cache.get("test_get_or_set"), None)
        self.assertEqual(self.cache.get_or_set("test_get_or_set", "value1"), 'value1')
        self.assertIsNone(self.cache.get("test_get_or_set"), 'value1')

    def test_default_used_when_none_is_set(self):
        self.assertIsNone(self.cache.set("test_default_used_when_none_is_set", None))
        self.assertIsNone(self.cache.get("test_default_used_when_none_is_set"))

    def test_datatype__bool(self):
        self.assertIsNone(self.cache.set("test_datatype__bool", True))

    def test_datatype_str(self):
        self.assertIsNone(self.cache.set("test_datatype_str", 'string'))

    def test_datatype_int(self):
        self.assertIsNone(self.cache.set("test_datatype_int", 123))

    def test_datatype_float(self):
        self.assertIsNone(self.cache.set("test_datatype_float", 1.23))

    def test_datatype_date(self):
        self.assertIsNone(self.cache.set("test_datatype_date", datetime.date.today()))

    def test_datatype_datetime(self):
        self.assertIsNone(self.cache.set("test_datatype_datetime", datetime.datetime.now()))

    def test_datatype_list(self):
        self.assertIsNone(self.cache.set("test_datatype_list", [1, 2, 3, 500, 4]))

    def test_datatype_tuple(self):
        self.assertIsNone(self.cache.set("test_datatype_tuple", (1, 2, 3, 500, 4)))

    def test_datatype_dict_simples(self):
        self.assertIsNone(self.cache.set("test_datatype_dict_simples", {'a': 1, 'b': '1', 'c': 2.0}))

    def test_delete(self):
        self.assertIsNone(self.cache.set("test_delete", "spam"))

    def test_close(self):
        self.assertTrue(hasattr(self.cache, "close"))
        self.cache.close()

    def test_unicode(self):
        # Unicode values can be cached
        stuff = {
            # "ascii": "ascii_value",
            # "unicode_ascii": "Iñtërnâtiônàlizætiøn1",
            "Iñtërnâtiônàlizætiøn": "Iñtërnâtiônàlizætiøn2",
            "ascii3": {"x": 1},
            # "ascii2": {"x": 1},
        }

        # Test `set`
        for key, value in stuff.items():
            with self.subTest(key=key):
                self.assertIsNone(self.cache.set(key, value))

        # Test `add`
        for (key, value) in stuff.items():
            with self.subTest(key=key):
                self.assertTrue(self.cache.add(key, value), True)

        # Test `delete`
        for (key, value) in stuff.items():
            self.assertIsNone(self.cache.delete(key))

        # Test `set_many`
        self.assertIsNone(self.cache.set_many(stuff))

    def test_binary_string(self):
        # Binary strings should be cacheable
        from zlib import compress

        value = "value_to_be_compressed"
        compressed_value = compress(value.encode())

        # Test set
        self.assertIsNone(self.cache.set("binary1-set", compressed_value))

        # Test add
        self.assertTrue(self.cache.add("binary1-add", compressed_value))

        # Test `delete`
        self.assertIsNone(self.cache.delete("binary1-add"))

        # Test set_many
        self.assertIsNone(self.cache.set_many({"binary1-set_many": compressed_value}))

    def test_get_many(self):
        pass

    def test_set_many(self):
        pass

    def test_delete_many(self):
        pass

    def test_clear(self):
        # The cache can be emptied using clear
        self.cache.set_many({"test_clear1": "spam", "test_clear2": "eggs"})
        self.cache.clear()

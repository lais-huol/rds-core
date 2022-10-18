import datetime
from bds_framework.cache import caches


class TestCacheMixin:

    def __init__(self, method_name: str = 'runTest') -> None:
        from bds_framework.cache.nocache import NoCache
        self.cache = NoCache()
        self.cache_name = 'default'
        super().__init__(method_name)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.cache.clear()

    def test_key_exists(self):
        self.assertFalse(self.cache.key_exists("test_has_key"))
        self.cache.add("test_has_key", 'value')
        self.assertTrue(self.cache.key_exists("test_has_key"))

    def test_add(self):
        self.assertTrue(self.cache.add("test_add", "value"))
        self.assertEqual(self.cache.get("test_add"), "value")
        self.assertFalse(self.cache.add("test_add", "value"))

    def test_get(self):
        self.assertTrue(self.cache.add("test_get", "value1"))
        self.assertEqual(self.cache.get("test_get"), 'value1')
        self.assertIsNone(self.cache.get("test_get_invalid"))
        self.assertEqual(self.cache.get("test_get_invalid", 'value1'), 'value1')

    def test_set(self):
        self.assertIsNone(self.cache.set("test_set", "value1"))
        self.assertEqual(self.cache.get("test_set"), 'value1')

    def test_get_or_set(self):
        self.assertIsNone(self.cache.get("test_get_or_set"), None)
        self.assertEqual(self.cache.get_or_set("test_get_or_set", "value1"), 'value1')
        self.assertEqual(self.cache.get("test_get_or_set"), 'value1')

    def test_default_used_when_none_is_set(self):
        """If None is cached, get() returns it instead of the default."""
        self.cache.set("test_default_used_when_none_is_set", None)
        self.assertIsNone(self.cache.get("test_default_used_when_none_is_set"))
        self.assertEqual(self.cache.get("test_default_used_when_none_is_set", default="default"), "default")

    def test_datatype__bool(self):
        self.cache.set("test_datatype__bool", True)
        self.assertTrue(self.cache.get("test_datatype__bool"))
        self.cache.set("test_datatype__bool", False)
        self.assertFalse(self.cache.get("test_datatype__bool"))

    def test_datatype_str(self):
        self.cache.set("test_datatype_str", 'string')
        self.assertEqual(self.cache.get("test_datatype_str"), 'string')

    def test_datatype_int(self):
        self.cache.set("test_datatype_int", 123)
        self.assertEqual(self.cache.get("test_datatype_int"), 123)

    def test_datatype_float(self):
        self.cache.set("test_datatype_float", 1.23)
        self.assertEqual(self.cache.get("test_datatype_float"), 1.23)

    def test_datatype_date(self):
        hoje = datetime.date.today()
        self.cache.set("test_datatype_date", hoje)
        self.assertEqual(self.cache.get("test_datatype_date"), hoje.isoformat())

    def test_datatype_datetime(self):
        agorinha = datetime.datetime.now()
        self.cache.set("test_datatype_datetime", agorinha)
        self.assertEqual(self.cache.get("test_datatype_datetime"), agorinha.isoformat())

    def test_datatype_list(self):
        self.cache.set("test_datatype_list", [1, 2, 3, 500, 4])
        self.assertEqual(self.cache.get("test_datatype_list"), [1, 2, 3, 500, 4])

    def test_datatype_tuple(self):
        self.cache.set("test_datatype_tuple", (1, 2, 3, 500, 4))
        self.assertEqual(self.cache.get("test_datatype_tuple"), [1, 2, 3, 500, 4])

    def test_datatype_dict_simples(self):
        d = {'a': 1, 'b': '1', 'c': 2.0}
        self.cache.set("test_datatype_dict_simples", d)
        self.assertEqual(self.cache.get("test_datatype_dict_simples"), d)

    def test_datatype_dict_complexo(self):
        hoje = datetime.date.today()
        agorinha = datetime.datetime.now()
        complex_dict_vai = {
            "test_datatype__bool_None": None,
            "test_datatype__bool_True": True,
            "test_datatype__bool_False": False,
            "test_datatype_str": 'string',
            "test_datatype_int": 123,
            "test_datatype_float": 1.23,
            "test_datatype_date": hoje,
            "test_datatype_datetime": agorinha,
            "test_datatype_list": [1, 2, 3, 500, 4],
            "test_datatype_tuple": (1, 2, 3, 500, 4),
        }

        complex_dict_voltar = {
            "test_datatype__bool_None": None,
            "test_datatype__bool_True": True,
            "test_datatype__bool_False": False,
            "test_datatype_str": 'string',
            "test_datatype_int": 123,
            "test_datatype_float": 1.23,
            "test_datatype_date": hoje.isoformat(),
            "test_datatype_datetime": agorinha.isoformat(),
            "test_datatype_list": [1, 2, 3, 500, 4],
            "test_datatype_tuple": [1, 2, 3, 500, 4],
        }

        self.cache.set("test_datatype_dict_complexo", complex_dict_vai)
        self.assertEqual(self.cache.get("test_datatype_dict_complexo"), complex_dict_voltar)

    def test_prefix(self):
        self.cache.set("somekey", "value")
        self.assertEqual(caches[self.cache_name].get("somekey"), "value")

    def test_delete(self):
        self.assertIsNone(self.cache.set("test_delete", "spam"))
        self.assertEqual(self.cache.get("test_delete"), "spam")
        self.assertIsNone(self.cache.delete("test_delete"))
        self.assertIsNone(self.cache.get("test_delete"))
        self.assertIsNone(self.cache.delete("test_delete"))

    def test_close(self):
        self.assertTrue(hasattr(self.cache, "close"))
        self.cache.close()

    # def test_unicode(self):
    #     # Unicode values can be cached
    #     stuff = {
    #         # "ascii": "ascii_value",
    #         # "unicode_ascii": "Iñtërnâtiônàlizætiøn1",
    #         "Iñtërnâtiônàlizætiøn": "Iñtërnâtiônàlizætiøn2",
    #         "ascii3": {"x": 1},
    #         # "ascii2": {"x": 1},
    #     }
    #
    #     # Test `set`
    #     for key, value in stuff.items():
    #         with self.subTest(key=key):
    #             self.cache.set(key, value)
    #             self.assertEqual(self.cache.get(key), value)
    #             self.cache.delete(key)
    #
    #     # Test `add`
    #     for (key, value) in stuff.items():
    #         with self.subTest(key=key):
    #             self.assertIs(self.cache.delete(key), True)
    #             self.assertIs(self.cache.add(key, value), True)
    #             self.assertEqual(self.cache.get(key), value)
    #
    #     # Test `set_many`
    #     for (key, value) in stuff.items():
    #         self.assertIs(self.cache.delete(key), True)
    #     self.cache.set_many(stuff)
    #     for (key, value) in stuff.items():
    #         with self.subTest(key=key):
    #             self.assertEqual(self.cache.get(key), value)

    def test_binary_string(self):
        # # Binary strings should be cacheable
        # from zlib import compress, decompress
        #
        # value = "value_to_be_compressed"
        # compressed_value = compress(value.encode())
        #
        # # Test set
        # self.cache.set("binary1", compressed_value)
        # compressed_result = self.cache.get("binary1")
        # self.assertEqual(compressed_value, compressed_result)
        # self.assertEqual(value, decompress(compressed_result).decode())
        #
        # # Test add
        # self.assertIs(self.cache.add("binary1-add", compressed_value), True)
        # compressed_result = self.cache.get("binary1-add")
        # self.assertEqual(compressed_value, compressed_result)
        # self.assertEqual(value, decompress(compressed_result).decode())
        #
        # # Test set_many
        # self.cache.set_many({"binary1-set_many": compressed_value})
        # compressed_result = self.cache.get("binary1-set_many")
        # self.assertEqual(compressed_value, compressed_result)
        # self.assertEqual(value, decompress(compressed_result).decode())
        pass

    def test_get_many(self):
        self.cache.set("tgm_a", "a")
        self.cache.set("tgm_b", "b")
        self.cache.set("tgm_c", "c")
        self.cache.set("tgm_d", "d")
        self.cache.set("tgm_x", None)
        self.cache.set("tgm_y", 1)
        self.assertEqual(self.cache.get_many(["tgm_a", "tgm_c", "tgm_d"]), {"tgm_a": "a", "tgm_c": "c", "tgm_d": "d"})
        self.assertEqual(self.cache.get_many(["tgm_a", "tgm_b", "tgm_e"]), {"tgm_a": "a", "tgm_b": "b"})
        self.assertEqual(self.cache.get_many(iter(["tgm_a", "tgm_b", "tgm_e"])), {"tgm_a": "a", "tgm_b": "b"})
        self.assertEqual(self.cache.get_many(["tgm_x", "tgm_y"]), {"tgm_x": None, "tgm_y": 1})
        self.assertEqual(self.cache.get_many(["tgm_p", "tgm_t"]), {})

    def test_set_many(self):
        self.cache.set_many({"tsm_a": "a", "tsm_b": "b", "tsm_c": "c", "tsm_d": "d"})
        self.assertEqual(self.cache.get_many(["tsm_a", "tsm_c", "tsm_d"]), {"tsm_a": "a", "tsm_c": "c", "tsm_d": "d"})
        self.assertEqual(self.cache.get_many(["tsm_a", "tsm_b", "tsm_e"]), {"tsm_a": "a", "tsm_b": "b"})
        self.assertEqual(self.cache.get_many(iter(["tsm_a", "tsm_b", "tsm_e"])), {"tsm_a": "a", "tsm_b": "b"})
        self.cache.set_many({"tsm_x": None, "tsm_y": 1})
        self.assertEqual(self.cache.get("tsm_x"), None)
        self.assertEqual(self.cache.get_many(["tsm_x", "tsm_y"]), {"tsm_x": None, "tsm_y": 1})
        self.assertIsNone(self.cache.set_many({}))

    def test_delete_many(self):
        self.cache.set_many({"tdm_1": "spam", "tdm_2": "eggs", "tdm_3": "ham"})
        self.cache.delete_many(["tdm_1", "tdm_2"])
        self.assertIsNone(self.cache.get("tdm_1"))
        self.assertIsNone(self.cache.get("tdm_2"))
        self.assertEqual(self.cache.get("tdm_3"), "ham")
        self.assertIsNone(self.cache.delete_many([]))

    def test_clear(self):
        # The cache can be emptied using clear
        self.cache.set_many({"test_clear1": "spam", "test_clear2": "eggs"})
        self.cache.clear()
        self.assertIsNone(self.cache.get("test_clear1"))
        self.assertIsNone(self.cache.get("test_clear2"))

    def test_incr(self):
        # The cache can be emptied using clear
        self.cache.set("test_incr", 1)
        self.assertEqual(self.cache.get("test_incr"), 1)
        self.assertEqual(self.cache.incr("test_incr"), 2)
        self.assertEqual(self.cache.incr("test_incr", 2), 4)

    def test_decr(self):
        # The cache can be emptied using clear
        self.cache.set("test_decr", 4)
        self.assertEqual(self.cache.get("test_decr"), 4)
        self.assertEqual(self.cache.decr("test_decr"), 3)
        self.assertEqual(self.cache.decr("test_decr", 2), 1)

    # def test_long_ttl(self):
    #     """
    #     Follow memcached's convention where a ttl greater than 30 days is
    #     treated as an absolute expiration timestamp instead of a relative
    #     offset (#12399).
    #     """
    #     self.cache.set("key1", "eggs", 60 * 60 * 24 * 30 + 1)  # 30 days + 1 second
    #     self.assertEqual(self.cache.get("key1"), "eggs")
    #
    #     self.assertIs(self.cache.add("key2", "ham", 60 * 60 * 24 * 30 + 1), True)
    #     self.assertEqual(self.cache.get("key2"), "ham")
    #
    #     self.cache.set_many(
    #         {"key3": "sausage", "key4": "lobster bisque"}, 60 * 60 * 24 * 30 + 1
    #     )
    #     self.assertEqual(self.cache.get("key3"), "sausage")
    #     self.assertEqual(self.cache.get("key4"), "lobster bisque")
    #
    # def test_forever_ttl(self):
    #     """
    #     Passing in None into ttl results in a value that is cached forever
    #     """
    #     self.cache.set("key1", "eggs", None)
    #     self.assertEqual(self.cache.get("key1"), "eggs")
    #
    #     self.assertIs(self.cache.add("key2", "ham", None), True)
    #     self.assertEqual(self.cache.get("key2"), "ham")
    #     self.assertIs(self.cache.add("key1", "new eggs", None), False)
    #     self.assertEqual(self.cache.get("key1"), "eggs")
    #
    #     self.cache.set_many({"key3": "sausage", "key4": "lobster bisque"}, None)
    #     self.assertEqual(self.cache.get("key3"), "sausage")
    #     self.assertEqual(self.cache.get("key4"), "lobster bisque")
    #
    #     self.cache.set("key5", "belgian fries", ttl=1)
    #     self.assertIs(self.cache.touch("key5", ttl=None), True)
    #     time.sleep(2)
    #     self.assertEqual(self.cache.get("key5"), "belgian fries")
    #
    # def test_zero_ttl(self):
    #     """
    #     Passing in zero into ttl results in a value that is not cached
    #     """
    #     self.cache.set("key1", "eggs", 0)
    #     self.assertIsNone(self.cache.get("key1"))
    #
    #     self.assertIs(self.cache.add("key2", "ham", 0), True)
    #     self.assertIsNone(self.cache.get("key2"))
    #
    #     self.cache.set_many({"key3": "sausage", "key4": "lobster bisque"}, 0)
    #     self.assertIsNone(self.cache.get("key3"))
    #     self.assertIsNone(self.cache.get("key4"))
    #
    #     self.cache.set("key5", "belgian fries", ttl=5)
    #     self.assertIs(self.cache.touch("key5", ttl=0), True)
    #     self.assertIsNone(self.cache.get("key5"))
    #
    # def test_float_ttl(self):
    #     # Make sure a ttl given as a float doesn't crash anything.
    #     self.cache.set("key1", "spam", 100.2)
    #     self.assertEqual(self.cache.get("key1"), "spam")
    #
    # def test_set_many_expiration(self):
    #     # set_many takes a second ``ttl`` parameter
    #     self.cache.set_many({"key1": "spam", "key2": "eggs"}, 1)
    #     time.sleep(2)
    #     self.assertIsNone(self.cache.get("key1"))
    #     self.assertIsNone(self.cache.get("key2"))
    #
    # def test_expiration(self):
    #     # Cache values can be set to expire
    #     self.cache.set("expire1", "very quickly", 1)
    #     self.cache.set("expire2", "very quickly", 1)
    #     self.cache.set("expire3", "very quickly", 1)
    #
    #     time.sleep(2)
    #     self.assertIsNone(self.cache.get("expire1"))
    #
    #     self.assertIs(self.cache.add("expire2", "newvalue"), True)
    #     self.assertEqual(self.cache.get("expire2"), "newvalue")
    #     self.assertIs(self.cache.has_key("expire3"), False)
    #
    # def test_touch(self):
    #     # default_cache.touch() updates the ttl.
    #     self.cache.set("expire1", "very quickly", ttl=1)
    #     self.assertIs(self.cache.touch("expire1", ttl=4), True)
    #     time.sleep(2)
    #     self.assertIs(self.cache.has_key("expire1"), True)
    #     time.sleep(3)
    #     self.assertIs(self.cache.has_key("expire1"), False)
    #     # default_cache.touch() works without the ttl argument.
    #     self.cache.set("expire1", "very quickly", ttl=1)
    #     self.assertIs(self.cache.touch("expire1"), True)
    #     time.sleep(2)
    #     self.assertIs(self.cache.has_key("expire1"), True)
    #
    #     self.assertIs(self.cache.touch("nonexistent"), False)

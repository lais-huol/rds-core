import time
import unittest
from bds_framework.cache import default_cache, caches


def f():
    return 42


class C:
    def m(n):
        return 24


class NoCacheTests(unittest.TestCase):
    # The Dummy cache backend doesn't really behave like a test backend, so it has its own test case.

    def test_simple(self):
        """  Dummy cache backend ignores cache set calls """
        default_cache.set("key", "value")
        self.assertIsNone(default_cache.get("key"))

    def test_add(self):
        "Add doesn't do anything in dummy cache backend"
        self.assertIs(default_cache.add("addkey1", "value"), True)
        self.assertIs(default_cache.add("addkey1", "newvalue"), True)
        self.assertIsNone(default_cache.get("addkey1"))

    def test_non_existent(self):
        "Nonexistent keys aren't found in the dummy cache backend"
        self.assertIsNone(default_cache.get("does_not_exist"))
        self.assertEqual(default_cache.get("does_not_exist", "bang!"), "bang!")

    def test_get_many(self):
        "get_many returns nothing for the dummy cache backend"
        default_cache.set_many({"a": "a", "b": "b", "c": "c", "d": "d"})
        self.assertEqual(default_cache.get_many(["a", "c", "d"]), {})
        self.assertEqual(default_cache.get_many(["a", "b", "e"]), {})

    # def test_get_many_invalid_key(self):
    #     msg = KEY_ERRORS_WITH_MEMCACHED_MSG % ":1:key with spaces"
    #     with self.assertWarnsMessage(CacheKeyWarning, msg):
    #         default_cache.get_many(["key with spaces"])

    def test_delete(self):
        "Cache deletion is transparently ignored on the dummy cache backend"
        default_cache.set_many({"key1": "spam", "key2": "eggs"})
        self.assertIsNone(default_cache.get("key1"))
        self.assertIs(default_cache.delete("key1"), False)
        self.assertIsNone(default_cache.get("key1"))
        self.assertIsNone(default_cache.get("key2"))

    def test_has_key(self):
        "The has_key method doesn't ever return True for the dummy cache backend"
        default_cache.set("hello1", "goodbye1")
        self.assertIs(default_cache.has_key("hello1"), False)
        self.assertIs(default_cache.has_key("goodbye1"), False)

    def test_in(self):
        "The in operator doesn't ever return True for the dummy cache backend"
        default_cache.set("hello2", "goodbye2")
        self.assertNotIn("hello2", default_cache)
        self.assertNotIn("goodbye2", default_cache)

    def test_incr(self):
        "Dummy cache values can't be incremented"
        default_cache.set("answer", 42)
        with self.assertRaises(ValueError):
            default_cache.incr("answer")
        with self.assertRaises(ValueError):
            default_cache.incr("does_not_exist")
        with self.assertRaises(ValueError):
            default_cache.incr("does_not_exist", -1)

    def test_decr(self):
        "Dummy cache values can't be decremented"
        default_cache.set("answer", 42)
        with self.assertRaises(ValueError):
            default_cache.decr("answer")
        with self.assertRaises(ValueError):
            default_cache.decr("does_not_exist")
        with self.assertRaises(ValueError):
            default_cache.decr("does_not_exist", -1)

    def test_touch(self):
        """Dummy cache can't do touch()."""
        self.assertIs(default_cache.touch("whatever"), False)

    def test_data_types(self):
        "All data types are ignored equally by the dummy cache"
        tests = {
            "string": "this is a string",
            "int": 42,
            "bool": True,
            "list": [1, 2, 3, 4],
            "tuple": (1, 2, 3, 4),
            "dict": {"A": 1, "B": 2},
            "function": f,
            "class": C,
        }
        for key, value in tests.items():
            with self.subTest(key=key):
                default_cache.set(key, value)
                self.assertIsNone(default_cache.get(key))

    def test_expiration(self):
        "Expiration has no effect on the dummy cache"
        default_cache.set("expire1", "very quickly", 1)
        default_cache.set("expire2", "very quickly", 1)
        default_cache.set("expire3", "very quickly", 1)

        time.sleep(2)
        self.assertIsNone(default_cache.get("expire1"))

        self.assertIs(default_cache.add("expire2", "newvalue"), True)
        self.assertIsNone(default_cache.get("expire2"))
        self.assertIs(default_cache.has_key("expire3"), False)

    def test_unicode(self):
        "Unicode values are ignored by the dummy cache"
        stuff = {
            "ascii": "ascii_value",
            "unicode_ascii": "Iñtërnâtiônàlizætiøn1",
            "Iñtërnâtiônàlizætiøn": "Iñtërnâtiônàlizætiøn2",
            "ascii2": {"x": 1},
        }
        for (key, value) in stuff.items():
            with self.subTest(key=key):
                default_cache.set(key, value)
                self.assertIsNone(default_cache.get(key))

    def test_set_many(self):
        "set_many does nothing for the dummy cache backend"
        self.assertEqual(default_cache.set_many({"a": 1, "b": 2}), [])

    # def test_set_many_invalid_key(self):
    #     msg = KEY_ERRORS_WITH_MEMCACHED_MSG % ":1:key with spaces"
    #     with self.assertWarnsMessage(CacheKeyWarning, msg):
    #         default_cache.set_many({"key with spaces": "foo"})

    def test_delete_many(self):
        "delete_many does nothing for the dummy cache backend"
        default_cache.delete_many(["a", "b"])

    # def test_delete_many_invalid_key(self):
    #     msg = KEY_ERRORS_WITH_MEMCACHED_MSG % ":1:key with spaces"
    #     with self.assertWarnsMessage(CacheKeyWarning, msg):
    #         default_cache.delete_many(["key with spaces"])

    def test_clear(self):
        "clear does nothing for the dummy cache backend"
        default_cache.clear()

    def test_get_or_set(self):
        self.assertEqual(default_cache.get_or_set("mykey", "default"), "default")
        self.assertIsNone(default_cache.get_or_set("mykey", None))

    def test_get_or_set_callable(self):
        def my_callable():
            return "default"

        self.assertEqual(default_cache.get_or_set("mykey", my_callable), "default")
        self.assertEqual(default_cache.get_or_set("mykey", my_callable()), "default")

import time
import unittest

import dynaconf
import opensearchpy
import pytest

from dynaconf.vendor.box.exceptions import BoxKeyError

from rds_core.searchengine import (
    create_index_if_not_exists, delete_index_if_exists,
    get_search_engine_config, search_engine, search_engine_healthy,
    index, query, search,
    # dsl_connection,
)


class TestSearchEngine(unittest.TestCase):

    def __init__(self, method_nname: str = 'runTest'):
        self.test_index = 'test_index'
        super(TestSearchEngine, self).__init__(methodName=method_nname)

    def setUp(self):
        create_index_if_not_exists(self.test_index)

    def tearDown(self):
        delete_index_if_exists(self.test_index)

    def test_double_create_index(self):
        self.assertFalse(create_index_if_not_exists(self.test_index))

    def test_invalid_index_creation(self):
        with self.assertRaises(Exception):
            create_index_if_not_exists(self.test_index, fail=True)

    def test_delete_index_not_exists(self):
        self.assertFalse(delete_index_if_exists('nem_criei_ainda'))

    def test_invalid_index_deletion(self):
        with self.assertRaises(Exception):
            delete_index_if_exists('nem_criei_ainda', params={'ignore_unavailable': False})

    def test_get_search_engine_config_valid(self):
        self.assertIsInstance(get_search_engine_config(), dynaconf.utils.boxing.DynaBox)
        self.assertIsInstance(get_search_engine_config('default'), dynaconf.utils.boxing.DynaBox)

    def test_get_search_engine_config__invalid(self):
        with self.assertRaises(BoxKeyError):
            self.assertIsNone(get_search_engine_config('fail'))

    # @openmock
    # def test_dsl_connection(self):
    #     self.assertEqual(dsl_connection(), unittest.TestCase)
    #     self.assertEqual(dsl_connection('default'), unittest.TestCase)
    #     # self.assertEqual(dsl_connection('does-not-exist'), unittest.TestCase)

    def test_search_engine(self):
        self.assertIsInstance(search_engine(), opensearchpy.OpenSearch)
        self.assertIsInstance(search_engine('default'), opensearchpy.OpenSearch)

    def test_search_engine__invalid(self):
        with self.assertRaises(BoxKeyError):
            search_engine('fail')

    def test_search_engine_healthy(self):
        self.assertTrue(search_engine_healthy())
        self.assertTrue(search_engine_healthy(alias='default'))

    def test_search_engine_healthy__invalid(self):
        with self.assertRaises(BoxKeyError):
            search_engine_healthy(alias='fail')

    # @openmock
    def test_index_document(self):
        self.assertIsInstance(index(self.test_index, {'username': 'admin', 'firstname': 'Admin'}), dict)
        self.assertIsInstance(index(self.test_index, {'username': 'admin', 'firstname': 'Admin'}), dict)
        self.assertIsInstance(index(self.test_index, {'username': 'admin', 'firstname': 'Admin'}, '1'), dict)
        self.assertIsInstance(index(self.test_index, {'username': 'admin', 'firstname': 'Admin'}, '2', alias='default'), dict)

    def test_query(self):
        index(self.test_index, {'username': 'admin', 'firstname': 'Admin'})
        time.sleep(2)  # como é próximo ao real, tem que esperar terminar de indexar
        result, count = query(self.test_index, 'admin')
        self.assertEqual(count, 1)

        index(self.test_index, {'username': 'admin', 'firstname': 'Admin2'}, alias='default')
        time.sleep(2)
        result, count = query(self.test_index, 'admin')
        self.assertEqual(count, 2)

    def test_search(self):
        index(self.test_index, {'username': 'admin', 'firstname': 'Admin'})
        time.sleep(2)  # como é próximo ao real, tem que esperar terminar de indexar
        body = {
            'size': 5,
            'query': {
                'multi_match': {
                    'query': 'admin',
                }
            }
        }
        result, count = search(self.test_index, body)
        self.assertEqual(count, 1)

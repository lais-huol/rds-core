import unittest
import pytest
from rds_framework.helpers import get_class, instantiate_class, get_variable_by_pathname
from rds_framework.helpers.cnes import is_cpf_or_cns
from rds_framework.helpers.http_client import HTTPException, get, get_json

TEST_DEFAULT_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': 'cnes.datasus.gov.br',
    'Referer': 'http://cnes.datasus.gov.br/pages/estabelecimentos/consulta.jsp',
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36',
}


class TestHelpersInit(unittest.TestCase):

    def test_get_class(self):
        self.assertEqual(get_class('unittest.TestCase'), unittest.TestCase)

    def test_instantiate_class(self):
        self.assertIsInstance(instantiate_class('unittest.TestCase'), unittest.TestCase)

    def test_get_variable_by_pathname(self):
        self.assertTrue(get_variable_by_pathname('unittest.__unittest'))


class TestHelpersCnes(unittest.TestCase):

    def test_is_cpf_or_cns__cpf(self):
        self.assertEqual(is_cpf_or_cns('12345678901'), 'cpf')

    def test_is_cpf_or_cns__cns(self):
        self.assertEqual(is_cpf_or_cns('123456789012345'), 'cns')

    def test_is_cpf_or_cns__no_one(self):
        with pytest.raises(Exception):
            is_cpf_or_cns('12345678901234')


class TestHelpersHttpClient(unittest.TestCase):

    def test_HTTPExceptionCustom(self):
        e = HTTPException('message', 'url', 'status_code', 'reason', [], [])
        self.assertEqual(str(e), 'message')
        self.assertEqual(e.url, 'url')
        self.assertEqual(e.status_code, 'status_code')
        self.assertEqual(e.reason, 'reason')
        self.assertEqual(e.request_headers, [])
        self.assertEqual(e.response_headers, [])

    def test_HTTPExceptionDefaults(self):
        e = HTTPException('message', 'url')
        self.assertIsNone(e.status_code)
        self.assertIsNone(e.reason)
        self.assertIsNone(e.request_headers)
        self.assertIsNone(e.response_headers)

    def test_get__valid(self):
        self.assertEqual(
            get('http://cnes.datasus.gov.br/services/gestao', TEST_DEFAULT_HEADERS, timeout=5),
            '{"D":"DUPLA","E":"ESTADUAL","M":"MUNICIPAL"}'
        )

    def test_get__invalid(self):
        with pytest.raises(HTTPException):
            get('http://cnes.datasus.gov.br/services/errado', TEST_DEFAULT_HEADERS, timeout=5)

    def test_get_json__valid(self):
        self.assertEqual(
            get_json('http://cnes.datasus.gov.br/services/gestao', TEST_DEFAULT_HEADERS, timeout=5),
            {"D": "DUPLA", "E": "ESTADUAL", "M": "MUNICIPAL"}
        )

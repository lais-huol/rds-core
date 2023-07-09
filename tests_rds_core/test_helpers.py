import unittest
import pytest
from rds.core.helpers import get_class, instantiate_class, get_variable_by_pathname
from rds.core.helpers.http_client import HTTPException, get, get_json

TEST_DEFAULT_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "",
    "Host": "cnes.datasus.gov.br",
    "Referer": "http://cnes.datasus.gov.br/pages/estabelecimentos/consulta.jsp",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
}


class TestHelpersInit(unittest.TestCase):
    def test_get_class(self):
        self.assertEqual(get_class("unittest.TestCase"), unittest.TestCase)

    def test_instantiate_class(self):
        self.assertIsInstance(instantiate_class("unittest.TestCase"), unittest.TestCase)

    def test_get_variable_by_pathname(self):
        self.assertTrue(get_variable_by_pathname("unittest.__unittest"))


class TestHelpersHttpClient(unittest.TestCase):
    def test_HTTPExceptionCustom(self):
        e = HTTPException("message", "url", "status_code", "reason", [], [])
        self.assertEqual(str(e), "message")
        self.assertEqual(e.url, "url")
        self.assertEqual(e.status_code, "status_code")
        self.assertEqual(e.reason, "reason")
        self.assertEqual(e.request_headers, [])
        self.assertEqual(e.response_headers, [])

    def test_HTTPExceptionDefaults(self):
        e = HTTPException("message", "url")
        self.assertIsNone(e.status_code)
        self.assertIsNone(e.reason)
        self.assertIsNone(e.request_headers)
        self.assertIsNone(e.response_headers)

    def test_get__valid(self):
        self.assertEqual(
            get(
                "http://cnes.datasus.gov.br/services/gestao",
                TEST_DEFAULT_HEADERS,
                timeout=5,
            ),
            '{"D":"DUPLA","E":"ESTADUAL","M":"MUNICIPAL"}',
        )

    def test_get__invalid(self):
        with pytest.raises(HTTPException):
            get(
                "http://cnes.datasus.gov.br/services/errado",
                TEST_DEFAULT_HEADERS,
                timeout=5,
            )

    def test_get_json__valid(self):
        self.assertEqual(
            get_json(
                "http://cnes.datasus.gov.br/services/gestao",
                TEST_DEFAULT_HEADERS,
                timeout=5,
            ),
            {"D": "DUPLA", "E": "ESTADUAL", "M": "MUNICIPAL"},
        )

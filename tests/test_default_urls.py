# coding=utf-8

import json
import unittest

from . import py3_skip
from .instances import frontik_re_app, frontik_test_app


class TestDefaultUrls(unittest.TestCase):
    @py3_skip
    def test_version(self):
        xml = frontik_test_app.get_page_xml('version')
        test_app_version = xml.xpath('application[@name="tests.projects.test_app"]/app-version/@number')[0]

        self.assertEqual(xml.tag, 'versions')
        self.assertEqual('last version', test_app_version)

    @py3_skip
    def test_unknown_version(self):
        xml = frontik_re_app.get_page_xml('version')
        re_app_version = xml.findtext('application[@name="tests.projects.re_app"]/version')

        self.assertEqual('unknown', re_app_version)

    @py3_skip
    def test_no_version(self):
        xml = frontik_re_app.get_page_xml('version')
        re_app_version = xml.findtext('application[@name="tests.projects.re_app"]/version')

        self.assertEqual(xml.tag, 'versions')
        self.assertEqual(re_app_version, 'unknown')

    @py3_skip
    def test_status(self):
        response = frontik_test_app.get_page('status')

        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=UTF-8')

        json_response = json.loads(response.content)
        self.assertIn('pages served', json_response)
        self.assertIn('http requests made', json_response)
        self.assertIn('bytes from http requests', json_response)
        self.assertIn('uptime', json_response)

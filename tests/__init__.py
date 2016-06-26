# coding=utf-8

import os

FRONTIK_ROOT = os.path.dirname(os.path.dirname(__file__))


def tearDownModule():
    from .instances import frontik_broken_app, frontik_non_debug, frontik_re_app, frontik_test_app
    from .test_http_client_keep_alive import frontik_keep_alive_app

    frontik_broken_app.stop()
    frontik_non_debug.stop()
    frontik_re_app.stop()
    frontik_test_app.stop()
    frontik_keep_alive_app.stop()

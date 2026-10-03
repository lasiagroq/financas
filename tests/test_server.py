"""Dependency-free smoke tests for the local Delícias da JU server."""

import http.client
import threading
import unittest

from main import create_server


class LocalServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server("127.0.0.1", 0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_home_page_is_served(self):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
        connection.request("GET", "/")
        response = connection.getresponse()
        body = response.read().decode()
        connection.close()

        self.assertEqual(response.status, 200)
        self.assertIn("Delícias da JU", body)
        self.assertIn('src="script.js"', body)

    def test_static_assets_are_served(self):
        for path, expected_type in (("/styles.css", "text/css"), ("/script.js", "text/javascript")):
            with self.subTest(path=path):
                connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
                connection.request("GET", path)
                response = connection.getresponse()
                response.read()
                connection.close()

                self.assertEqual(response.status, 200)
                self.assertIn(expected_type, response.getheader("Content-Type"))

import unittest
from vats_proxy import ProxyManager


class ProxyManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.manager = ProxyManager(count=3)

    def test_multiple_proxy(self):
        """Test multiple proxies"""
        # if proxy list includes 3 proxy
        result = len(self.manager.proxies)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
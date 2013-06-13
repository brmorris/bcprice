import unittest, sys, os

g_script_dirname = os.path.dirname(os.path.realpath(__file__))
g_configfile = os.path.expanduser("~") + "/.bcprice" + "/bcprice.ini"
sys.path.append("%s/../.." % ( g_script_dirname ))

import BCCPrice.utils as utils
import BCCPrice.Price as bcprice

class PriceTestCase(unittest.TestCase):
    def setUp(self):
        self.sanity = "sanity" 

    def tearDown(self):
        self.check = None

    def test_sanity(self):
        self.assertEqual(self.sanity, "sanity", 'sanity check')

    def test_price(self):
        prices = bcprice.Price(configFile = g_configfile)
        nw = prices.nw
        self.assertEqual(prices.currency, "USD", 'USD is default currency')
        self.assertEqual(prices.durations[0], "24h", '24h is default duration')

    def test_getPricesForCurrency(self):
        prices = bcprice.Price(configFile = g_configfile)
        pbyc1 = prices.getPricesForCurrency()
        self.assertIsNotNone(pbyc1, 'getPricesForCurrency result')

    def test_getPricesForTimeframe(self):
        prices = bcprice.Price(configFile = g_configfile)
        pbytf1 = prices.getPricesForTimeframe()
        self.assertIsNotNone(pbytf1, 'getPricesForTimeframe 1 - default')
        pbytf2 = prices.getPricesForTimeframe(timeframe="30d")
        self.assertIsNotNone(pbytf2, 'getPricesForTimeframe 2 - non-default timeframe')

    def test_getIntervals(self):
        prices = bcprice.Price(configFile = g_configfile)
        intervals = prices.getIntervals()
        self.assertIsNotNone(intervals, 'getIntervals result')

    def test_getDataPoints(self):
        prices = bcprice.Price(configFile = g_configfile)
        dataPoints = prices.getDataPoints()
        self.assertIsNotNone(dataPoints[0], 'getIntervals result')

if __name__ == '__main__':
    unittest.main()
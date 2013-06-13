import unittest

import BCCPrice.termgraph as termgraph
import BCCPrice.utils as utils
import BCCPrice.Price as bcprice

class PriceTestCase(unittest.TestCase):
    def setUp(self):
        self.check = "check price data" # Widget('The widget')

    def tearDown(self):
        self.check = None

    def test_sanity(self):
        self.assertEqual(self.check, "check price data", 'sanity check')

    def test_price(self):
        prices = bcprice.Price()
        nw = prices.nw
        self.assertEqual(prices.currency, "USD", 'USD is default currency')
        self.assertEqual(prices.durations[0], "24h", '24h is default duration')

    def test_getPricesForCurrency(self):
        prices = bcprice.Price()
        pbyc1 = prices.getPricesForCurrency()
        self.assertIsNotNone(pbyc1, 'getPricesForCurrency result')

    def test_getPricesForTimeframe(self):
        prices = bcprice.Price()
        pbytf1 = prices.getPricesForTimeframe()
        self.assertIsNotNone(pbytf1, 'getPricesForTimeframe 1 - default')
        pbytf2 = prices.getPricesForTimeframe(timeframe="30d")
        self.assertIsNotNone(pbytf2, 'getPricesForTimeframe 2 - non-default timeframe')

    def test_getIntervals(self):
        prices = bcprice.Price()
        intervals = prices.getIntervals()
        self.assertIsNotNone(intervals, 'getIntervals result')

    def test_getDataPoints(self):
        prices = bcprice.Price()
        dataPoints = prices.getDataPoints()
        self.assertIsNotNone(dataPoints[0], 'getIntervals result')

if __name__ == '__main__':
    unittest.main()
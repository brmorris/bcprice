import BCCPrice.utils as utils
import pdb

class Price(object):
    def __init__(self, endpoint='http://api.bitcoincharts.com/v1/weighted_prices.json', currency="USD", configFile=None):
        self.nw = utils.Load().Network(configFile = configFile)
        self.data = self.nw.get_json(endpoint)
        self.durations = ['24h', ' 7d', '30d']
        self.currency = currency

    def getPricesForCurrency(self):
        pbyc = self.data[self.currency]
        pbyc["currency"] = self.currency
        return pbyc

    def getPricesForTimeframe(self, timeframe="24h"):
        pbyc = self.getPricesForCurrency()
        return pbyc[timeframe]

    def getIntervals(self):
        # todo: this could be filtered by argument, and also include cached results based on time
        return self.durations

    def getDataPoints(self):
        # fixme: generalize to self.getIntervals
        currency_price = self.getPricesForCurrency()
        return [float(currency_price['24h']), float(currency_price['7d']), float(currency_price['30d'])] 
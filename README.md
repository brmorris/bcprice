=======
bcprice
=======

A python command-line tool that outputs latest [Bitcoin](http://bitcoin.org/) market prices in the terminal using the [Bitcoin Charts Api](http://bitcoincharts.com/about/markets-api). The tool supports:

 - Formatted output
 - JSON output
 - (Very) simple graphs
 - Multiple currencies/timeframes
 - HTTP request caching with configurable expiration

Installation
============

Grab the source from github and install it:

    git clone git://github.com/brmorris/bcprice.git && cd bcprice && python setup.py install

Examples
========

 - Show the weighted market price for the last day, week and month:

        $  bcprice
        24h 108.81
        07d 104.99
        30d 116.09

 - Show the weighted market prices for the last week in Australian dollars. Specifiying `-s|--short` will just return the raw market data (useful when calling `bcprice` in other scripts):
  
        $  bcprice  -c AUD -t  7d  -s
        115.19

 - Same query exported as JSON:
 
        $ bcprice -c AUD  -j
        {"currency": "AUD", "7d": "115.19", "30d": "123.17", "24h": "118.59"}`

 - Show output as super simple graph:
 
        $ bcprice -c AUD -g
        24h: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 118.59
        7d:  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 115.19
        30d: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 123.17
 
 - Use `--format` to specify the exact output string format:
 
        $ bcprice -c EUR --format "Today's price in euros is %(24h)s"
    	Today's price in euros is 83.20

Usage
=====

Here's the usage statement:

    $ bcprice  --help
    Usage: bcprice [options]
   
    Options:
    
      -h, --help            show this help message and exit
      -g, --graph           draw a simple graph
      -s, --short           minimal output (useful for calling by scripts)
      -j, --json            json output (combine with currency)
      -c CURRENCY, --currency=CURRENCY
                            output currency
      -t TIMEFRAME, --timeframe=TIMEFRAME
                            price timeframe, either 24h | 7d | 30d
      -f FORMAT, --format=FORMAT
                        specify output format using tokens: (%24h)s (%7d)s (%30d)s (%currency)s
      -d, --debug           debug output

Configuration
=============

Configuration is stored in ini format at `~/.bcprice/bcprice.ini`. If the tool can't find the configuration it generates it with this configuration:

    $ cat ~/.bcprice/bcprice.ini
    [bcprice]
    # default format
    format = 24h: %(24h)s %(currency)s
    7d: %(7d)s
    30d: %(30d)s
    # default currency
    currency = USD
    # default weighted price timeframe
    timeframe = 24h
    # width in chars of the graph
    graph_width = 50
    
    [network]
    # http request cache expiration in seconds
    cache_expire = 300

Tests
=====

There are some app unit tests which can be run via

    $ python  lib/BCCPrice/test/test_price.py
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.022s
    
    OK

TODO
====

I may or may not ever get around to these TODOs but a few ideas to take it further

* interface to bitcoin chart telnet service 
* complete coverage of the bitcoin chart Api (history and market data)
* watch mode (ala top) using curses
* expose/export historical data via the network cache. this might not add value in this instance, 
  but other users of the utils class might find it useful
* make the graphs more interesting/flexible


Versions
========

* Ver 0.5.0 - Jun 12, 2013 - Initial version





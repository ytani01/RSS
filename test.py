#!/usr/bin/env python3
#
"""
"""
__author__ = 'Yoichi Tanibayashi'
__date__   = '2020'

import feedparser

from MyLogger import get_logger

class Test:
    def __init__(self, url, debug):
        self._dbg = debug
        self._lgr = get_logger(__class__.__name__, self._dbg)
        self._lgr.debug('url=%s', url)

        self._url = url
        self._rss_data = feedparser.parse(self._url)

    def main(self):
        self._lgr.debug('')

        for ent in self._rss_data.entries:
            print(ent['title'])

    def end(self):
        self._lgr.debug('')


import click
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS,
               help="""
""")
@click.argument('url', type=str)
@click.option('--debug', '-d', 'debug', is_flag=True, default=False,
              help='debug flag')
def main(url, debug):
    _lgr = get_logger(__name__, debug)
    _lgr.debug('url=%s', url)

    _lgr.info('start')

    app = Test(url, debug=debug)

    try:
        app.main()
    finally:
        _lgr.debug('finally')
        app.end()
        _lgr.debug('end')


if __name__ == '__main__':
    main()

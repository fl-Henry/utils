import argparse

from threading import Lock


class SingletonMeta(type):

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Args(metaclass=SingletonMeta):

    def __init__(self):
        parser = argparse.ArgumentParser(description='Recipe scraper + translater.')
        parser.add_argument('--scrape', '-s', help='To scrape the recipes.', action='store_true')
        parser.add_argument('--translate', '-t', help='To translate the recipes.',
                            type=str, choices=['deepl', 'deepl_web', 'ai', 'google', None], default=None)
        parser.add_argument('--lang', '-l', help='Language to scrape to. (not implemented)', type=str, default='UK')

        args = parser.parse_args()

        # parse argument
        self.scrape: bool = args.scrape
        self.translate: str = args.translate
        self.lang: str = args.lang

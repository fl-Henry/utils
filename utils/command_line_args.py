import argparse


parser = argparse.ArgumentParser(description='Recipe scraper + translater.')
parser.add_argument('--scrape', '-s', help='To scrape the recipes.', action='store_true')
parser.add_argument('--translate', '-t', help='To translate the recipes.',
                    type=str, choices=['deepl', 'deepl_web', 'ai', 'google', None], default=None)
parser.add_argument('--lang', '-l', help='Language to scrape to. (not implemented)', type=str, default='UK')

args = vars(parser.parse_args())


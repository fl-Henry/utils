"""
This module defines command-line arguments for the application.

The script uses the `argparse` module to parse and handle command-line arguments, which control
the behavior of the application.
The parsed arguments are stored in a dictionary (`args`), making it easy to access the values of the
command-line options. This dictionary can be used elsewhere in the program to control the execution
of the recipe scraping and translation process.


Example:
- `--scrape` or `-s`: A flag that, when provided, tells the application to scrape recipes.
- `--translate` or `-t`: Specifies the translation service to use for the recipes. Possible values include:
    - `'deepl'`: Use DeepL for translation.
    - `'deepl_web'`: Use DeepL's web interface for translation.
    - `'ai'`: Use an AI-based translation service.
    - `'google'`: Use Google Translate.
    - `None`: Default value, indicating no translation (not implemented).
- `--lang` or `-l`: Specifies the language to scrape the recipes to. The default is `'UK'`, though this feature is not yet implemented.

Example usage:
    python script.py --scrape --translate deepl --lang 'FR'
"""

import argparse

parser = argparse.ArgumentParser(description='Recipe scraper + translater.')
parser.add_argument('--scrape', '-s', help='To scrape the recipes.', action='store_true')
parser.add_argument('--translate', '-t', help='To translate the recipes.',
                    type=str, choices=['deepl', 'deepl_web', 'ai', 'google', None], default=None)
parser.add_argument('--lang', '-l', help='Language to scrape to. (not implemented)', type=str, default='UK')

args = vars(parser.parse_args())

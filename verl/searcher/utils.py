import os

from .web_searcher import WebSearcher
from .web_search_en import WebSearcherEnglish
from .web_search_zh import WebSearcherChinese

def create_web_searcher(language: str, api_key: str = None) -> WebSearcher:
    language = language.lower()
    if language == "en":
        return WebSearcherEnglish(api_key)
    elif language == "zh":
        return WebSearcherChinese(api_key)
    else:
        raise ValueError("Unsupported language: {}".format(language))
    
from .wiki_searcher import WikiSearcher

def create_wiki_searcher(language: str, url: str = None) -> WikiSearcher:
    index_name = "wiki_" + language.lower()
    url = url or os.environ.get('ELASTIC_SEARCH_URL')
    if url:
        return WikiSearcher(index_name, url)
    else:
        return WikiSearcher(index_name)
from .web_searcher import WebSearcher

from .web_search_en import WebSearcherEnglish
from .web_search_zh import WebSearcherChinese

def create_web_searcher(language: str, api_key: str = None) -> WebSearcher:
    language = language.lower()
    if language == "english":
        return WebSearcherEnglish(api_key)
    elif language == "chinese":
        return WebSearcherChinese(api_key)
    else:
        raise ValueError("Unsupported language: {}".format(language))
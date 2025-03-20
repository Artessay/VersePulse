import pytest
import elasticsearch

from verl.searcher import create_web_searcher, create_wiki_searcher


def test_english_web_searcher():
    web_searcher = create_web_searcher("en")
    assert web_searcher is not None
    result = web_searcher.search("why is the sky blue?")
    assert isinstance(result, list)


def test_chinese_web_searcher():
    web_searcher = create_web_searcher("zh")
    assert web_searcher is not None
    # result = web_searcher.search("为什么天空是蓝色的？")
    # assert isinstance(result, list)

def test_unsupported_language():
    with pytest.raises(ValueError):
        create_web_searcher("unsupported")


def test_english_wiki_searcher():
    wiki_searcher = create_wiki_searcher("en")
    assert wiki_searcher is not None
    result = wiki_searcher.search("why is the sky blue?")
    assert isinstance(result, list)


def test_chinese_wiki_searcher():
    wiki_searcher = create_wiki_searcher("zh")
    assert wiki_searcher is not None
    result = wiki_searcher.search("为什么天空是蓝色的？")
    assert isinstance(result, list)

def test_unsupported_language():
    wiki_searcher = create_wiki_searcher("unsupported")
    assert wiki_searcher is not None
    with pytest.raises(elasticsearch.NotFoundError):
        wiki_searcher.search("why is the sky blue?")
import pytest

from search import create_web_searcher


def test_english_web_searcher():
    web_searcher = create_web_searcher("english")
    result = web_searcher.search("why is the sky blue?")
    assert isinstance(result, list)


def test_chinese_web_searcher():
    web_searcher = create_web_searcher("chinese")
    assert web_searcher is not None
    # result = web_searcher.search("为什么天空是蓝色的？")
    # assert isinstance(result, list)

def test_unsupported_language():
    with pytest.raises(ValueError):
        create_web_searcher("unsupported")
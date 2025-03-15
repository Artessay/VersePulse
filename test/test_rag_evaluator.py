import math
from langchain_openai import ChatOpenAI

from search import RetrievalQualityEvaluator

def test_rag_evaluator():
    llm = ChatOpenAI(
        model="qwen2.5-1.5b-instruct",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    user_input = "When and Where Albert Einstein was born?"
    retrieved_contexts = [
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]

    rag_evaluator = RetrievalQualityEvaluator(llm)
    score = rag_evaluator.evaluate_retrieval(user_input, retrieved_contexts)

    assert math.isclose(score, 1.0, abs_tol=1e-3)
    
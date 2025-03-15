import math
from langchain_openai import ChatOpenAI

from search import RetrievalQualityEvaluator

def test_rag_evaluator():
    llm = ChatOpenAI(
        model="qwen2.5-1.5b-instruct",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    user_input = "When and Where Albert Einstein was born?"

    rag_evaluator = RetrievalQualityEvaluator(llm)

    # completely relevant
    retrieved_contexts_1 = [
        "Albert Einstein was born March 14, 1879.",
        "Albert Einstein was born at Ulm, in Württemberg, Germany.",
    ]
    evaluation_result = rag_evaluator.evaluate_retrieval(user_input, retrieved_contexts_1)
    assert math.isclose(evaluation_result, 1.0)

    # not relevant
    retrieved_contexts_2 = [
        "Wikis are powered by wiki software, also known as wiki engines.",
        "There are hundreds of thousands of wikis in use, both public and private.",
    ]
    evaluation_result = rag_evaluator.evaluate_retrieval(user_input, retrieved_contexts_2)
    assert math.isclose(evaluation_result, 0.0)

    # partially relevant
    retrieved_contexts_3 = [
        "Born in the German Empire, Einstein moved to Switzerland in 1895",
        "Wikis are powered by wiki software, also known as wiki engines.",
    ]
    evaluation_result = rag_evaluator.evaluate_retrieval(user_input, retrieved_contexts_3)
    assert math.isclose(evaluation_result, 0.5)
    
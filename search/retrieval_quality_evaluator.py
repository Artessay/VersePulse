import pandas as pd
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_relevancy

class RAGRetrievalQualityEvaluator:
    def __init__(self):
        # 初始化评估所需的指标
        self.metrics = [answer_relevancy, context_relevancy]

    def evaluate_retrieval(self, questions, retrieved_contexts, answers):
        """
        评估 RAG 检索质量

        :param questions: 用户提出的问题列表
        :param retrieved_contexts: 检索到的上下文列表，每个元素对应一个问题的检索结果
        :param answers: 生成的答案列表，每个元素对应一个问题的答案
        :return: 评估结果
        """
        # 确保输入的列表长度一致
        if len(questions) != len(retrieved_contexts) != len(answers):
            raise ValueError("问题、检索到的上下文和答案的列表长度必须一致")

        # 创建 DataFrame 来存储评估数据
        data = {
            "question": questions,
            "contexts": retrieved_contexts,
            "answer": answers
        }
        df = pd.DataFrame(data)

        # 进行评估
        result = evaluate(df, metrics=self.metrics)

        return result


# 示例使用
if __name__ == "__main__":
    # 示例问题
    questions = [
        "什么是人工智能？",
        "机器学习有哪些常见算法？"
    ]
    # 示例检索到的上下文
    retrieved_contexts = [
        ["人工智能是一门研究如何使计算机能够模拟人类智能的学科。"],
        ["机器学习常见算法包括决策树、支持向量机等。"]
    ]
    # 示例生成的答案
    answers = [
        "人工智能是模拟人类智能的学科。",
        "常见算法有决策树和支持向量机。"
    ]

    evaluator = RAGRetrievalQualityEvaluator()
    evaluation_result = evaluator.evaluate_retrieval(questions, retrieved_contexts, answers)
    print(evaluation_result)
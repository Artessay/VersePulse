---
license: CC-BY-NC-SA-4.0
text:
  question-answering:
    language:
      - en
    
configs:
- config_name: nq
  data_files:
  - split: train
    path: "nq/train.jsonl"
  - split: dev
    path: "nq/dev.jsonl"
  - split: test
    path: "nq/test.jsonl"
- config_name: triviaqa
  data_files:
  - split: train
    path: "triviaqa/train.jsonl"
  - split: dev
    path: "triviaqa/dev.jsonl"
  - split: test
    path: "triviaqa/test.jsonl"
- config_name: popqa
  data_files:
  - split: test
    path: "popqa/test.jsonl"
- config_name: squad
  data_files:
  - split: train
    path: "squad/train.jsonl"
  - split: dev
    path: "squad/dev.jsonl"
- config_name: msmarco-qa
  data_files:
  - split: train
    path: "ms_marco/train.jsonl"
  - split: dev
    path: "ms_marco/dev.jsonl"
- config_name: narrativeqa
  data_files:
  - split: train
    path: "narrativeqa/train.jsonl"
  - split: dev
    path: "narrativeqa/dev.jsonl"
  - split: test
    path: "narrativeqa/test.jsonl"
- config_name: wikiqa
  data_files:
  - split: train
    path: "wiki_qa/train.jsonl"
  - split: dev
    path: "wiki_qa/dev.jsonl"
  - split: test
    path: "wiki_qa/test.jsonl"
- config_name: web_questions
  data_files:
  - split: train
    path: "web_questions/train.jsonl"
  - split: test
    path: "web_questions/test.jsonl"
- config_name: ambig_qa
  data_files:
  - split: train
    path: "ambig_qa/train.jsonl"
  - split: dev
    path: "ambig_qa/dev.jsonl"
- config_name: siqa
  data_files:
  - split: train
    path: "siqa/train.jsonl"
  - split: dev
    path: "siqa/dev.jsonl"
- config_name: commenseqa
  data_files:
  - split: train
    path: "commonsense_qa/train.jsonl"
  - split: dev
    path: "commonsense_qa/dev.jsonl"
- config_name: boolq
  data_files:
  - split: train
    path: "boolq/train.jsonl"
  - split: dev
    path: "boolq/dev.jsonl"
- config_name: piqa
  data_files:
  - split: train
    path: "piqa/train.jsonl"
  - split: dev
    path: "piqa/dev.jsonl"
- config_name: fermi
  data_files:
  - split: train
    path: "fermi/train.jsonl"
  - split: dev
    path: "fermi/dev.jsonl"
  - split: test
    path: "fermi/test.jsonl"
- config_name: hotpotqa
  data_files:
  - split: train
    path: "hotpotqa/train.jsonl"
  - split: dev
    path: "hotpotqa/dev.jsonl"
- config_name: 2wikimultihopqa
  data_files:
  - split: train
    path: "2wikimultihopqa/train.jsonl"
  - split: dev
    path: "2wikimultihopqa/dev.jsonl"
- config_name: musique
  data_files:
  - split: train
    path: "musique/train.jsonl"
  - split: dev
    path: "musique/dev.jsonl"
- config_name: bamboogle
  data_files:
  - split: test
    path: "bamboogle/test.jsonl"
- config_name: asqa
  data_files:
  - split: train
    path: "asqa/train.jsonl"
  - split: dev
    path: "asqa/dev.jsonl"
- config_name: eli5
  data_files:
  - split: train
    path: "eli5/train.jsonl"
  - split: dev
    path: "eli5/dev.jsonl"
- config_name: wikiasp
  data_files:
  - split: train
    path: "wikiasp/train.jsonl"
  - split: dev
    path: "wikiasp/dev.jsonl"
  - split: test
    path: "wikiasp/test.jsonl"
- config_name: mmlu
  data_files:
  - split: train
    path: "mmlu/train.jsonl"
  - split: dev
    path: "mmlu/dev.jsonl"
  - split: test
    path: "mmlu/test.jsonl"
  - split: 5_shot
    path: "mmlu/5_shot.jsonl"
- config_name: truthful_qa
  data_files:
  - split: dev
    path: "truthful_qa/dev.jsonl"
- config_name: hellaswag
  data_files:
  - split: train
    path: "hellaswag/train.jsonl"
  - split: dev
    path: "hellaswag/dev.jsonl"
- config_name: arc
  data_files:
  - split: train
    path: "arc/train.jsonl"
  - split: dev
    path: "arc/dev.jsonl"
  - split: test
    path: "arc/test.jsonl"
- config_name: openbookqa
  data_files:
  - split: train
    path: "openbookqa/train.jsonl"
  - split: dev
    path: "openbookqa/dev.jsonl"
  - split: test
    path: "openbookqa/test.jsonl"
- config_name: fever
  data_files:
  - split: train
    path: "fever/train.jsonl"
  - split: dev
    path: "fever/dev.jsonl"
- config_name: wow
  data_files:
  - split: train
    path: "wow/train.jsonl"
  - split: dev
    path: "wow/dev.jsonl"
- config_name: wned
  data_files:
  - split: dev
    path: "wned/dev.jsonl"
- config_name: t-rex
  data_files:
  - split: train
    path: "trex/train.jsonl"
  - split: dev
    path: "trex/dev.jsonl"
- config_name: zero-shot_re
  data_files:
  - split: train
    path: "zsre/train.jsonl"
  - split: dev
    path: "zsre/dev.jsonl"
- config_name: ay2
  data_files:
  - split: train
    path: "ay2/train.jsonl"
  - split: dev
    path: "ay2/dev.jsonl"
- config_name: curatedtrec
  data_files:
  - split: train
    path: "curatedtrec/train.jsonl"
  - split: test
    path: "curatedtrec/test.jsonl"
- config_name: quartz
  data_files:
  - split: train
    path: "quartz/train.jsonl"
  - split: test
    path: "quartz/test.jsonl"
  - split: dev
    path: "quartz/dev.jsonl"
---

# ⚡FlashRAG: A Python Toolkit for Efficient RAG Research

FlashRAG is a Python toolkit for the reproduction and development of Retrieval Augmented Generation (RAG) research. Our toolkit includes 32 pre-processed benchmark RAG datasets and 13 state-of-the-art RAG algorithms. 
With FlashRAG and provided resources, you can effortlessly reproduce existing SOTA works in the RAG domain or implement your custom RAG processes and components.

For more information, please view our GitHub repo and paper:

**GitHub repo**: [https://github.com/RUC-NLPIR/FlashRAG/](https://github.com/RUC-NLPIR/FlashRAG/)

**Huggingface Datasets**: [https://huggingface.co/datasets/RUC-NLPIR/FlashRAG_datasets/](https://huggingface.co/datasets/RUC-NLPIR/FlashRAG_datasets/tree/main)

**Paper link**: [FlashRAG: A Modular Toolkit for Efficient Retrieval-Augmented Generation Research](https://arxiv.org/abs/2405.13576).

# Dataset Card for FlashRAG Datasets

<!-- Provide a quick summary of the dataset. -->

We have collected and processed 35 datasets widely used in RAG research, pre-processing them to ensure a consistent format for ease of use. For certain datasets (such as Wiki-asp), we have adapted them to fit the requirements of RAG tasks according to the methods commonly used within the community.

## Dataset Details

For each dataset, we save each split as a `jsonl` file, and each line is a dict as follows:
```python
{
  'id': str,
  'question': str,
  'golden_answers': List[str],
  'metadata': dict
}
```

Below is the list of datasets along with the corresponding sample sizes:

| Task                      | Dataset Name    | Knowledge Source | # Train   | # Dev   | # Test |
|---------------------------|-----------------|------------------|-----------|---------|--------|
| QA                        | NQ              | wiki             | 79,168    | 8,757   | 3,610  |
| QA                        | TriviaQA        | wiki & web       | 78,785    | 8,837   | 11,313 |
| QA                        | PopQA           | wiki             | /         | /       | 14,267 |
| QA                        | SQuAD           | wiki             | 87,599    | 10,570  | /      |
| QA                        | MSMARCO-QA      | web              | 808,731   | 101,093 | /      |
| QA                        | NarrativeQA     | books and story  | 32,747    | 3,461   | 10,557 |
| QA                        | WikiQA          | wiki             | 20,360    | 2,733   | 6,165  |
| QA                        | WebQuestions    | Google Freebase  | 3,778     | /       | 2,032  |
| QA                        | AmbigQA         | wiki             | 10,036    | 2,002   | /      |
| QA                        | SIQA            | -                | 33,410    | 1,954   | /      |
| QA                        | CommonSenseQA      | -                | 9,741     | 1,221   | /      |
| QA                        | BoolQ           | wiki             | 9,427     | 3,270   | /      |
| QA                        | PIQA            | -                | 16,113    | 1,838   | /      |
| QA                        | Fermi           | wiki             | 8,000     | 1,000   | 1,000  |
| multi-hop QA              | HotpotQA        | wiki             | 90,447    | 7,405   | /      |
| multi-hop QA              | 2WikiMultiHopQA | wiki             | 15,000    | 12,576  | /      |
| multi-hop QA              | Musique         | wiki             | 19,938    | 2,417   | /      |
| multi-hop QA              | Bamboogle       | wiki             | /         | /       | 125    |
| multi-hop QA              | StrategyQA      | wiki             | 2290      | /       | /
| Long-form QA              | ASQA            | wiki             | 4,353     | 948     | /      |
| Long-form QA              | ELI5            | Reddit           | 272,634   | 1,507   | /      |
| Long-form QA              | WikiPassageQA            | wiki             | 3,332     | 417    |  416      |
| Open-Domain Summarization | WikiASP         | wiki             | 300,636   | 37,046  | 37,368 |
| multiple-choice           | MMLU            | -                | 99,842    | 1,531   | 14,042 |
| multiple-choice           | TruthfulQA      | wiki             | /         | 817     | /      |
| multiple-choice           | HellaSWAG       | ActivityNet      | 39,905    | 10,042  | /      |
| multiple-choice           | ARC             | -                | 3,370     | 869     | 3,548  |
| multiple-choice           | OpenBookQA      | -                | 4,957     | 500     | 500    |
| multiple-choice           | QuaRTz      | -                | 2696     | 384     | 784    |
| Fact Verification         | FEVER           | wiki             | 104,966   | 10,444  | /      |
| Dialog Generation         | WOW             | wiki             | 63,734    | 3,054   | /      |
| Entity Linking            | AIDA CoNll-yago | Freebase & wiki  | 18,395    | 4,784   | /      |
| Entity Linking            | WNED            | Wiki             | /         | 8,995   | /      |
| Slot Filling              | T-REx           | DBPedia          | 2,284,168 | 5,000   | /      |
| Slot Filling              | Zero-shot RE    | wiki             | 147,909   | 3,724   | /      |
| In-domain QA| DomainRAG | Web pages of RUC| / | / | 485|

## Retrieval Corpus

We also provide a corpus document library for retrieval, with the path in FlashRAG/retrieval-corpus. 
```jsonl
{"id":"0", "contents": "...."}
{"id":"1", "contents": "..."}
```
The `contents` key is essential for building the index. For documents that include both text and title, we recommend setting the value of `contents` to `{title}\n{text}`. The corpus file can also contain other keys to record additional characteristics of the documents.
Detail information of provided can be found in our github link: [https://github.com/RUC-NLPIR/FlashRAG?tab=readme-ov-file#document-corpus](https://github.com/RUC-NLPIR/FlashRAG?tab=readme-ov-file#document-corpus).

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

Please kindly cite our paper if helps your research:
```BibTex
@article{FlashRAG,
    author={Jiajie Jin and
            Yutao Zhu and
            Xinyu Yang and
            Chenghao Zhang and
            Zhicheng Dou},
    title={FlashRAG: A Modular Toolkit for Efficient Retrieval-Augmented Generation Research},
    journal={CoRR},
    volume={abs/2405.13576},
    year={2024},
    url={https://arxiv.org/abs/2405.13576},
    eprinttype={arXiv},
    eprint={2405.13576}
}
```

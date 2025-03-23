import argparse
from flashrag.config import Config
from flashrag.utils import get_dataset
from flashrag.pipeline import SequentialPipeline
from flashrag.prompt import PromptTemplate

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset_name", default="nq", type=str)
parser.add_argument("-g", "--generator_model", default="llama3-8b-instruct", type=str)
parser.add_argument("--gpu_id", default="0,1,2,3", type=str)
args = parser.parse_args()

config_dict = {
    "data_dir": "dataset/",
    "dataset_name": args.dataset_name,
    "generator_model": args.generator_model,
    "gpu_id": args.gpu_id,
}

config = Config(config_dict=config_dict)

all_split = get_dataset(config)
test_data = all_split["test"]
prompt_templete = PromptTemplate(
    config,
    system_prompt="Answer the question based on the given document. \
                    Only give me the answer and do not output any other words. \
                    \nThe following are given documents.\n\n{reference}",
    user_prompt="Question: {question}\nAnswer:",
)


pipeline = SequentialPipeline(config, prompt_template=prompt_templete)


output_dataset = pipeline.run(test_data, do_eval=True)
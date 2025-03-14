# VersePulse

VersePulse: Multimodal RAG Engine integrating Real-Time Search with LLMs for accurate, dynamic cross-modal content generation.

## Installation

Download the repository in your local machine.

```bash
git clone https://github.com/Artessay/VersePulse.git
cd VersePulse
```

Install the dependencies with conda. Note that we use flash attention 2 for faster inference, so you need to install it first seperately.

```bash
conda create -n verse-pulse python=3.11 -y
conda activate verse-pulse

pip install torch==2.5.1
pip install -e .

# flash attention 2, you can download it from https://github.com/Dao-AILab/flash-attention/releases
pip install flash_attn-2.7.4.post1+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
```

## Quick Start

### Login to Wandb

If you want to use Wandb logger, you need to login to Wandb first.

```bash
wandb login
```

### GRPO Training

We provide a series scripts to train LLMs on huggingface datasets. You can find them in `scripts/`.
For example, to train the Qwen2.5-3B model on the math12k dataset, you can run the following command.

```bash
bash scripts/run_qwen2_5_3b_math.sh
```

## Acknowledgement

We are grateful to the following repositories for their contributions.

- [EasyR1](https://github.com/hiyouga/EasyR1)
- [Search-R1](https://github.com/PeterGriffinJin/Search-R1)
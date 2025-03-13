# VersePulse

VersePulse: Multimodal RAG Engine integrating Real-Time Search with LLMs for accurate, dynamic cross-modal content generation.

## Installation

```bash
git clone https://github.com/Artessay/VersePulse.git
cd VersePulse
```

```bash
conda create -n verse-pulse python=3.11 -y
conda activate verse-pulse

pip install torch
pip install -e .

# flash attention 2
pip install flash_attn-2.7.4.post1+cu12torch2.5cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
```

## Quick Start

### GRPO Training

```bash
bash scripts/run_qwen2_5_vl_7b_geo.sh
```

## Acknowledgement

- [EasyR1](https://github.com/hiyouga/EasyR1)
- [Search-R1](https://github.com/PeterGriffinJin/Search-R1)
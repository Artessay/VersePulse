# Wikipedia

## Install environment

```bash
conda create -n wiki python=3.12 -y
conda activate wiki
pip install beir
```

## Build Wikipedia index

Download the Wikipedia dump from the [DPR repository](https://github.com/facebookresearch/DPR/blob/main/dpr/data/download_data.py#L32) using the following command:

```bash
mkdir -p data/dpr
wget -O data/dpr/psgs_w100.tsv.gz https://dl.fbaipublicfiles.com/dpr/wikipedia_split/psgs_w100.tsv.gz
pushd data/dpr
gzip -d psgs_w100.tsv.gz
popd
```

Download Elasticsearch engine:

```bash
cd data
wget -O elasticsearch-7.17.9.tar.gz https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.9-linux-x86_64.tar.gz  # download Elasticsearch
tar zxvf elasticsearch-7.17.9.tar.gz
rm elasticsearch-7.17.9.tar.gz 
mv elasticsearch-7.17.9 elasticsearch
cd ..
```

Run Elasticsearch:

```bash
cd data/elasticsearch
nohup bin/elasticsearch &  # run Elasticsearch in background
cd ../..
```

Use Elasticsearch to index the Wikipedia dump:

```bash
python elastic_build.py --data_path data/dpr/psgs_w100.tsv --index_name wiki  # build index
```

## Query Wikipedia

```bash
python elastic_query.py --query "Digital Economy" --index_name wiki --size 10
```
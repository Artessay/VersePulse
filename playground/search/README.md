# Wikipedia Corpus

## Download wikipedia dump

Download the corpus:


## Download Elasticsearch engine

Download Elasticsearch engine:

```bash
cd data
wget -O elasticsearch-7.17.9.tar.gz https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.17.9-linux-x86_64.tar.gz  # download Elasticsearch
tar zxvf elasticsearch-7.17.9.tar.gz
rm elasticsearch-7.17.9.tar.gz 
mv elasticsearch-7.17.9 elasticsearch
cd ..
```

## Build wikipedia index


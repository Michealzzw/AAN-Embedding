#!/bin/sh
if [ ! $1 ]; then
  echo "Please input AAN-Embedding path"
  echo "eg.: ./run_line ~/AAN-Embedding/"
else
git clone https://github.com/tangjianpku/LINE
cd LINE/linux
wget http://mirrors.ustc.edu.cn/gnu/gsl/gsl-2.3.tar.gz
tar -zxf gsl-2.3.tar.gz
cd gsl-2.3
sudo ./configure
sudo make
sudo make install
cd ..
LD_LIBRARY_PATH=/usr/local/lib
export LD_LIBRARY_PATH
input=~/AAN-Embedding/CitationNetwork/CitationNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CitationNetwork-1st-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CitationNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CitationNetwork-2nd-vec.tsv
./line -train $input -output $output -order 2 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CitationNetworkBi.tsv
output=~/AAN-Embedding/CitationNetwork/CitationNetworkBi-2nd-vec.tsv
./line -train $input -output $output -order 2 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CitationNetworkPlusCocitedNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CitationNetworkPlusCocitedNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CitationNetworkPlusCocitingNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CitationNetworkPlusCocitingNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CocitedNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CocitedNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationNetwork/CocitingNetwork.tsv
output=~/AAN-Embedding/CitationNetwork/CocitingNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Para2vec.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Para2vec-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Word2vec.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Word2vec-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-TFIDF.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-TFIDF-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-owner.tsv
output=~/AAN-Embedding/CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-owner-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-target.tsv
output=~/AAN-Embedding/CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-target-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Balance.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Balance-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Quality.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Quality-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Quantity.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Customer-Based-Quantity-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Balance.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Balance-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Quality.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Quality-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Quantity.tsv
output=~/AAN-Embedding/CitationContextSimilarityNetwork/Goods-Based-Quantity-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
fi

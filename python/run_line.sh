#!/bin/sh
wget http://mirrors.ustc.edu.cn/gnu/gsl/gsl-2.3.tar.gz
tar -zxf gsl-2.3.tar.gz
cd gsl-2.3
sudo ./configure
sudo make
sudo make install
cd ..
g++ -lm -pthread -Ofast -march=native -Wall -funroll-loops -ffast-math -Wno-unused-result line.cpp -o line -lgsl -lm -lgslcblas
LD_LIBRARY_PATH=/usr/local/lib
export LD_LIBRARY_PATH
input=../CitationNetwork/CitationNetwork.tsv
output=../CitationNetwork/CitationNetwork-1st-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationNetwork/CitationNetwork.tsv
output=../CitationNetwork/CitationNetwork-2nd-vec.tsv
./line -train $input -output $output -order 2 -samples 100 -threads 4
input=../CitationNetwork/CitationNetworkBi.tsv
output=../CitationNetwork/CitationNetworkBi-2nd-vec.tsv
./line -train $input -output $output -order 2 -samples 100 -threads 4
input=../CitationNetwork/CitationNetworkPlusCocitedNetwork.tsv
output=../CitationNetwork/CitationNetworkPlusCocitedNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationNetwork/CitationNetworkPlusCocitingNetwork.tsv
output=../CitationNetwork/CitationNetworkPlusCocitingNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationNetwork/CocitedNetwork.tsv
output=../CitationNetwork/CocitedNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationNetwork/CocitingNetwork.tsv
output=../CitationNetwork/CocitingNetwork-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Para2vec.tsv
output=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Para2vec-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Word2vec.tsv
output=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-Word2vec-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-TFIDF.tsv
output=../CitationContextSimilarityNetwork/CitationContextSimilarityNetwork-Cocited-TFIDF-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-owner.tsv
output=../CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-owner-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-target.tsv
output=../CitationContext-DocumentSimilarityNetwork/CitationContext-DocumentSimilarityNetwork-target-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Customer-Based-Balance.tsv
output=../CitationContextSimilarityNetwork/Customer-Based-Balance-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Customer-Based-Quality.tsv
output=../CitationContextSimilarityNetwork/Customer-Based-Quality-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Customer-Based-Quantity.tsv
output=../CitationContextSimilarityNetwork/Customer-Based-Quantity-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Goods-Based-Balance.tsv
output=../CitationContextSimilarityNetwork/Goods-Based-Balance-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Goods-Based-Quality.tsv
output=../CitationContextSimilarityNetwork/Goods-Based-Quality-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4
input=../CitationContextSimilarityNetwork/Goods-Based-Quantity.tsv
output=../CitationContextSimilarityNetwork/Goods-Based-Quantity-vec.tsv
./line -train $input -output $output -order 1 -samples 100 -threads 4

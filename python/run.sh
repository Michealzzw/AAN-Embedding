#!/bin/sh
if [ "$1" = "clean" ]; then
  cd ..
  rm -r CitationContext-DocumentSimilarityNetwork
  rm -r CitationContext2DocumentEmbedding
  rm -r CitationContextEmbedding
  rm -r CitationContextSimilarityNetwork
  rm -r CitationNetwork
  rm -r DocumentEmbedding
  rm -r Result
  cd python
else
  if [ "$1" = "install" ]; then
    cd ..
#    wget http://clair.eecs.umich.edu/aan/downloads/aandec2014.tar.gz
#    tar -zxf aandec2014.tar.gz
    mkdir CitationContext-DocumentSimilarityNetwork
    mkdir CitationContext2DocumentEmbedding
    mkdir CitationContextEmbedding
    mkdir CitationContextSimilarityNetwork
    mkdir CitationNetwork
    mkdir DocumentEmbedding
    mkdir Result
    cd python
    find ../2014/papers_text/ -name "*.txt" -o -name "*.body" > ../2014/paper_path.txt
  else
    echo "Starting"
  fi
  python dictionary.py
  python divide-paper-into-sentences.py
  python CitationContext2vec-TFIDF.py
  python CitationContext2Document-TFIDF.py

  #After Word2vec training
  python dictionary_vector.py
  python document2vec-Para2vec.py
  python document2vec-Word2vec.py
  python CitationNetwork.py
  python CitationContextSimilarityNetwork.py
  python CitationContext-DocumentSimilarityNetwork.py
  python CustomerGoodsModel.py
  echo "Finish"
  ./run_line.sh
  ./run_test.sh
fi

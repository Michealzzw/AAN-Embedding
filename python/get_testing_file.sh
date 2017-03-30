#!/bin/sh
find ../CitationContext-DocumentSimilarityNetwork/ -name "*-vec.tsv" >embedding_path.txt
find ../CitationContext2DocumentEmbedding/ -name "*.tsv" >>embedding_path.txt
find ../CitationContextSimilarityNetwork/ -name "*-vec.tsv" >>embedding_path.txt
find ../CitationNetwork/ -name "*-vec.tsv" >>embedding_path.txt


预处理完毕文件：
paper-vectors.txt Para2vec的vector
aan_testing.tsv 测试的link
CitationContext.tsv 引文内容


DocumentEmbedding
1. 不考虑citation生成的文本embedding
    1. TFIDF?
    2. word2vec
    3. para2vec ☑️

CitationContext2DocumentEmbedding
2. CitationContext组成的文本embedding
    1.  TFIDF☑️
    2. word2vec
    3. para2vec☑️
    4. OWNER+TARGET

CitationContextSimilarityNetwork
3. 根据CitationContext相关度组成的网络 (TFIDF,w2v,p2v)
    1. Co-cited TFIDF
    2. Co-cited w2v
    3. Co-cited p2v
    4. Co-citing?
    5. 顾客-商品模型
        1. 顾客一起用的越多越像
        2. 顾客一起用的评价越一致越像
        3. 商品一起被评价的顾客越多越像
        4. 商品被顾客评价越一致越像
        5. 一致度除以总的cite数

CitationContext-DocumentSimilarityNetwork
4. CitationContext和Paper 的相似度
    1. 与owner
    2. 与target

CitationNetwork
5. Citation网络
    1. 1order Citation Network ⭕️
    2. 2order Citation Network ⭕️
    3. 1+2 ?
    4. Co-cited
    5. Co-citing
    6. CN + Co-cited N ⭕️
    7. CN + Co-citing N ⭕️

Line-modify
6. 修改Line
    1. ab+bc+ca ？(等于ab，bc，ac三条边而已)
    2. abc


顾客消费行为得出顾客相似度
顾客点评得出商品相似度

AAN-Embedding
================
PKU Ziwei Zheng

运行
-----
#预处理完毕文件：
paper-vectors.txt Para2vec的vector<br>
aan_testing.tsv 测试的link<br>
CitationContext.tsv 引文内容<br>
##下载地址:https://pan.baidu.com/s/1bMDGJW
将文件解压在AAN-Embedding根目录，然后移到项目根目录<br>
mv AAN-Embedding-Data/* [项目目录的路径]<br>

#运行顺序：
cd python<br>
./run.sh install<br>
                    //得到部分Embedding和Network，如果想重新运行可以./run.sh clean后再次运行<br>
./run_line.sh [项目目录的绝对路径]<br>
                    // eg.: ~/AAN-Embedding/  用Line得出剩下的Embedding<br>
./run_test.sh<br>
                    //测试<br>

Embedding
-------
#DocumentEmbedding
##1. 不考虑citation生成的文本embedding
    1. TFIDF ☑️<br>
    2. word2vec ☑️<br>
    3. para2vec ☑️<br>

#CitationContext2DocumentEmbedding
##2. CitationContext组成的文本embedding
    1.  TFIDF☑️<br>
    2. word2vec ☑️<br>
    3. para2vec☑️<br>
    4. OWNER+TARGET✖️，指向不明<br>

#CitationContextSimilarityNetwork
##3. 根据CitationContext相关度组成的网络 (TFIDF,w2v,p2v)
    1. Co-cited TFIDF ☑️<br>
    2. Co-cited w2v ☑️<br>
    3. Co-cited p2v ☑️<br>
    4. Co-citing?<br>
    5. 顾客-商品模型<br>
        1. 顾客一起用的越多越像 co-citing/log(average())<br>
        2. 顾客一起用的评价越一致越像<br>
        3. 商品一起被评价的顾客越多越像 co-cited/log(average());<br>
        4. 商品被顾客评价越一致越像<br>
        5. 一致度除以总的cite数<br>
        顾客消费行为得出顾客相似度<br>
        顾客点评得出商品相似度<br>

#CitationContext-DocumentSimilarityNetwork
##4. CitationContext和Paper 的相似度
    1. 与owner ☑️<br>
    2. 与target ☑️<br>

#CitationNetwork
##5. Citation网络
    1. 1order Citation Network ☑️⭕️<br>
    2. 2order Citation Network ☑️⭕️<br>
    3. 1+2 ?<br>
    4. Co-cited☑️<br>
    5. Co-citing☑️<br>
    6. CN + Co-cited N ☑️⭕️<br>
    7. CN + Co-citing N ☑️⭕️<br>

#Line-modify
##6. 修改Line
    1. ab+bc+ca ？(等于ab，bc，ac三条边而已)<br>
    2. abc ⭕️<br>

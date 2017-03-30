AAN-Embedding
================
PKU Ziwei Zheng

运行
-----
### 预处理完毕文件：
paper-vectors.txt Para2vec的vector<br>
aan_testing.tsv 测试的link<br>
CitationContext.tsv 引文内容<br>
#### 下载地址:https://pan.baidu.com/s/1bMDGJW
将文件解压在AAN-Embedding根目录，然后移到项目根目录<br>
mv AAN-Embedding-Data/* [项目目录的路径]<br>

####  运行顺序：
    cd python
    ./run.sh install    //得到部分Embedding和Network，如果想重新运行可以./run.sh clean后再次运行
    ./run_line.sh [项目目录的绝对路径]     // eg.: ~/AAN-Embedding/  用Line得出剩下的Embedding
    ./run_test.sh                       //测试

Embedding
-------
### DocumentEmbedding
#### 1. 不考虑citation生成的文本embedding
    1. TFIDF ☑️
    2. word2vec ☑️
    3. para2vec ☑️

### CitationContext2DocumentEmbedding
#### 2. CitationContext组成的文本embedding
    1.  TFIDF☑️
    2. word2vec ☑️
    3. para2vec☑️
    4. OWNER+TARGET✖️，指向不明

### CitationContextSimilarityNetwork
#### 3. 根据CitationContext相关度组成的网络 (TFIDF,w2v,p2v)
    1. Co-cited TFIDF ☑️
    2. Co-cited w2v ☑️
    3. Co-cited p2v ☑️
    4. Co-citing?
    5. 顾客-商品模型
        1. 顾客一起用的越多越像 co-citing/log(average())
        2. 顾客一起用的评价越一致越像
        3. 商品一起被评价的顾客越多越像 co-cited/log(average());
        4. 商品被顾客评价越一致越像
        5. 一致度除以总的cite数
        顾客消费行为得出顾客相似度
        顾客点评得出商品相似度

### CitationContext-DocumentSimilarityNetwork
#### 4. CitationContext和Paper 的相似度
    1. 与owner ☑️
    2. 与target ☑️

### CitationNetwork
#### 5. Citation网络
    1. 1order Citation Network ☑️⭕️
    2. 2order Citation Network ☑️⭕️
    3. 1+2 ?
    4. Co-cited☑️
    5. Co-citing☑️
    6. CN + Co-cited N ☑️⭕️
    7. CN + Co-citing N ☑️⭕️

### Line-modify
#### 6. 修改Line
    1. ab+bc+ca ？(等于ab，bc，ac三条边而已)
    2. abc ⭕️

# Chinese-PPDB
Chineses PPDB (Chinses paraphrase database)是一个自动抽取大规模中文复述语料库。
复述是对相同语义的不同字面表述，是语言多样性的集中体现。
创建该语料库的目标是增强自然语言处理方法应对中文语言多样性的问题，提升模型的鲁棒性和泛化性。

与PPDB语料库类似，该语料库包含词汇、短语和模版三种粒度的复述数据。



Chineses PPDB是一个处于起步阶段的语料库，后续会不断的增加语料库的规模，包含的特征、不同的相似度度量的特征等。

# 文件格式
与PPDB不同，该语料库以JSON格式作为数据存储的主要格式，以便于后续的读取和使用。对于单条复述其格式如下：
'''json
{
    "phrase":phrase,
    "paraphrase":phrase,
    "from":"",
    "features":{},
    "alignment":"",
    "entailment":""
}
'''

其中phrase是词、短语或模版，paraphrase是对应的复述，from字段是该该数据的来源，目前的主要来源包含：双语平行数据、单语对齐数据。
features字段是对该复述对的一些特征，例如编辑距离、词向量相似度等，包含多种特征。特征的列表及其说明在文件中详细描述。
alignment字段是两个复述对在词一级的对齐；
entailment字段是参考PPDB给出的句子对是否为等价语义。

# 版权信息

该语料库免费向研究者使用。


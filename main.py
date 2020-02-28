# 加载Python自带 或通过pip安装的模块
import random
import jieba
import json
from gensim.models import Word2Vec
# from xpinyin import Pinyin
import jieba.analyse
import jieba.posseg
# 加载用户自己的模块
# from example_module import foo

# 对词性进行标注
def dosegment_all(sentence):
    '''
    带词性标注，对句子进行分词，不排除停词等
    :param sentence:输入字符
    :return:
    '''
    sentence_seged = jieba.posseg.cut(sentence.strip())
    outstr = ''
    for x in sentence_seged:
        outstr+="{}/{},".format(x.word,x.flag)
    #上面的for循环可以用python递推式构造生成器完成
    # outstr = ",".join([("%s/%s" %(x.word,x.flag)) for x in sentence_seged])
    return outstr

# ----------------------------------------
# 本地调试时使用的路径配置
#inp_path = '/Users/harry/tianchi_docs/benchmark_texts.txt'
#out_path = 'adversarial.txt'
# ----------------------------------------

# ----------------------------------------
# 提交时使用的路径配置（提交时请激活）
inp_path = './tcdata/benchmark_texts.txt'
out_path = './adversarial.txt'
# inp_path = './test_data/insult.txt'
# ----------------------------------------

# 加载模型
# en_wiki_word2vec_model = Word2Vec.load('./data/wiki.zh.text.model')
# p = Pinyin()
# thu1 = thulac.thulac(seg_only=True, model_path="./models")  # 设置模式为行分词模式

# 加载txt
with open(inp_path, 'r',encoding='UTF-8') as f:
    inp_lines = f.readlines()

# 分词 标注词性
'''
out_lines = []
for _line in inp_lines:
    a = dosegment_all(_line)
    s = a.split(',')
    seq = ''
    for items in s:
        word = ''
        get_pos = False
        for w in items:
            if get_pos == True:
                if (w == 'n') | (w == 'v'):
                    # word = p.get_pinyin(word,tone_marks='numbers')
                    try:
                        res = en_wiki_word2vec_model.most_similar(word)
                        word = res[0][0]
                    except KeyError:
                        break
                    break

            else:
                if w == '/':
                    get_pos = True
                else:
                    word = word + w
        seq = seq + word

    out_lines.append(seq)
'''
#    out_lines.append(seq)

#    print(seq)

def transform(line):
#     """转换一行文本。
# #     :param line: 对抗攻击前的输入文本
# #     :type line: str
# #     :returns: str -- 对抗攻击后的输出文门
# #     """
# #     # 修改以下逻辑
    insert_pool = list('1234567890')
    out_line = line.replace('\n', '') + random.choice(insert_pool)
    return out_line
# #
# #
out_lines = [transform(_line) for _line in inp_lines]


# out_lines = []
target = json.dumps({'text': out_lines}, ensure_ascii=False)
#
with open(out_path, 'w') as f:
     f.write(target)

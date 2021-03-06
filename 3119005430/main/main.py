from jieba import lcut
import re
import sys
import numpy as np
from memory_profiler import profile


# coding=utf-8
# 读取目标文档
@profile
def readText(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    # text = []
    # for line in f.readlines():  # 依次读取每行
    #     line = line.strip()  # 去掉每行头尾空白
    #     if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
    #         continue
    #     text.append(line)
    # text.sort()
    return text  # 排序后将文档返回


# 利用结巴算法对目标文档进行“分词”处理
@profile
def cut(text):
    words = []
    seg_list = lcut(text, cut_all=False)  # 使用jieba下的lcut()方法，精确分割，返回一个列表
    pat = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5]').sub(" ", "")  # 将正则表达式转换为内部格式，提高执行效率
    for word in seg_list:
        if re.match(pat, word):
            words.append(word)  # 筛选出不含标点符号的结果
        else:
            pass
    return words


# 对于两个文档中相同词语进行追加合并进列表

def mergeWords(t1, t2):
    MergeWords = []
    for i in t1:
        MergeWords.append(i)
    for i in t2:
        if i not in MergeWords:
            MergeWords.append(i)
    return MergeWords


# 分别统计两个文档关键词和词频并合并结果转化为向量（vector）

def countWords(MergeWords, t1, t2):
    list1 = [0 for i in range(len(MergeWords))]  # 设定长度并赋值为0
    count1 = dict(zip(MergeWords, list1))  # 设置一个具有合并后词列表的键，但值为零的字典
    for x in t1:
        if x in MergeWords:
            count1[x] += 1  # 遍历合并列表，计算出词频
        else:
            pass

    list2 = [0 for i in range(len(MergeWords))]
    count2 = dict(zip(MergeWords, list2))
    for y in t2:
        if y in MergeWords:
            count2[y] += 1
        else:
            pass
    vec1 = list(count1.values())  # 将字典转化为列表类型
    vec2 = list(count2.values())
    return vec1, vec2


# 通过向量计算余弦相似度（cosine_similarity）

def cosine_similarity(v1, v2):
    a = np.array(v1)  # 将向量列表转化为数组形式
    b = np.array(v2)
    ma = np.linalg.norm(a)  # np.linalg.norm()对数组求整体元素的平方和开根号
    mb = np.linalg.norm(b)
    sim = (np.matmul(a, b)) / (ma * mb)  # np.matmul()方法计算内积，结果为余弦相似度
    return sim


# 主函数，其包含调用其他函数

def Main(p1, p2, f) -> object:
    try:
        t1 = cut(readText(p1))
        t2 = cut(readText(p2))

        mw = mergeWords(t1, t2)
        v1, v2 = countWords(mw, t1, t2)
        result = cosine_similarity(v1, v2)
        result = np.float(result)*100
        result = round(result, 2)  # 保留小数点后两位
        print("文本相似度为："+str(result)+"%")
        fh = open(f, "a", encoding='utf-8')
        fh.write(str(p1) + "与" + str(p2) + "的相似度：" + str(result)+"%")
        fh.close()
    except FileNotFoundError:
        print("文件不存在！")


# 函数入口
if __name__ == '__main__':
    path1 = ""
    path2 = ""
    file_save = ""
    try:
        path1 = sys.argv[1] # 实现与命令行交互
        path2 = sys.argv[2]
        file_save = sys.argv[3]
    except IndexError:
        path1 = input("请输入正版文件路径：")
        path2 = input("请输入抄袭文件路径：")
        file_save = input("请输入你要保存结果的路径：")
    Main(path1, path2, file_save)

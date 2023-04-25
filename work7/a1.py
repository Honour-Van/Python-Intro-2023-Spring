n = int(input()) # 获取句子个数

# 构建单词与出现次数的字典
word_count = {}
sentences = []
for i in range(n):
    sentence = input().split()
    sentences.append(sentence)
    for word in sentence:
        word_count[word] = word_count.get(word, 0) + 1

# 将字典按照出现次数和字典序排序，并为每个单词分配一个序号
word_list = sorted(word_count.items(), key=lambda x: (x[1], x[0]))
word_dict = {word_list[i][0]: i for i in range(len(word_list))}

# 对输入的每个句子进行编码
for sentence in sentences:
    for j in range(len(sentence)):
        sentence[j] = str(word_dict[sentence[j]])
    print(' '.join(sentence))

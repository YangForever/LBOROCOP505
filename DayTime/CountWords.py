def Count(line):
    dic = {}
    contents = line.strip('\n').split(' ')
    for word in contents:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

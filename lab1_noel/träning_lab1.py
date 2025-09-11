def tokenize(x):
    words=[]
    start=0

    for i in x:
        while i[start]<len(i):
            if start.isspace():
                start+=1

    return words

print(tokenize(['Hej på er']))
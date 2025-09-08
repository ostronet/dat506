

text = ["detta, är en sträng", 'dett är en annan']

def tokenize(text):
    fixed_words = []
    for line in text:
        line = line + " "
        start = 0
        end = 0
        while start < len(line) and end < len(line):

            
            if line[end].isspace() == False:
                if line[end].isdigit() == True:
                    while line[end].isdigit() == True:
                        end += 1
                    fixed_words.append(line[start:end])
                    start = end

                if line[end].isalpha() == True:
                    while line[end].isalpha() == True:
                        end += 1
                    fixed_words.append(line[start:end].lower())
                    start = end
                elif line[end].isspace() == False:
                    end += 1
                    fixed_words.append(line[start:end].lower())
                    start = end
            else:
                end += 1
                start = end

        if end > start and line[end].isalpha() is True:
            fixed_words.append(line[start:end])

    return(fixed_words)

def countWords(words, stopWords):
    saved = {}
    for ord in words:
        if ord in stopWords:
            continue
        if ord not in saved:
            saved[ord] = 1
            continue
        if ord in saved:
            saved[ord] += 1

    return saved

def printTopMost(saved,n): 
    sorterad = sorted(saved.items(), key = lambda x: -x[1])[:n] 

    for ord,count in sorterad:
        w = ord.ljust(20)
        n = str(count).rjust(5)
        print(w+n)


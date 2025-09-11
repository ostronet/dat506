def tokenizer(rader):
    words=[]
    for rad in rader:
        start=0
        while start<len(rad):

            while rad[start].isspace():
                start+=1
            if start>=len(rad):
                    break

            if rad[start].isalpha():
                end=start
                while end<len(rad) and rad[start].isalpha():
                    end+=1
                words.append((rad[start:end]).lower())
                start=end

            if rad[start].isdigit():
                end=start
                while end<len(rad) and rad[start].isdigit():
                    end+=1
                words.append(rad[start:end])
                start=end

            else:
                words.append(rad[start])
                start+=1
    return words

print(tokenizer(['Jag heter Noel, det är vackert väder idag']))

#def countWords(words, stopWords):
   # par={}

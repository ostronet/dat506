def tokenize(lines):
    words = [] #tom lista där tokens fylls på
    for line in lines: #loopar för varje rad i dokumentet
        start = 0 #sätter startvärde till 0

        while start < len(line): #loopar längden av en rad för varje rad
            while start<len(line) and line[start].isspace(): #när blanksteg så hoppar den ett element fram
                start+=1
            if start>=len(line):
                break
            
            if line[start].isalpha(): #om elementet är en bokstav
                end=start #sätter första och sista elementet lika med varandra
                while end<len(line) and line[end].isalpha(): #så länge sista elementet är en bokstav på raden flyttas det ett steg
                   end+=1
                words.append((line[start:end].lower())) #sparar ordet, start till end, i listan
                start=end #sätter ny start till end

            elif line[start].isdigit():
                end=start
                while end<len(line) and line[end].isdigit():
                    end+=1
                words.append(line[start:end])
                start=end

            else:
                words.append(line[start])
                start +=1
                
    return words

def countWords(words, stopWords):
    lista={}
    for word in words:
        if word in stopWords:
         continue
        if word in lista:
            lista[word]+=1
        else:
           lista[word]=1
    return lista

def printTopMost(lista,n):
    sortera = sorted(lista.items(), key=lambda x: -x[1])[:n]
    for word, freq in sortera:
        w=word.ljust(20)
        n=str(freq).rjust(5)
        print(w+n)


            
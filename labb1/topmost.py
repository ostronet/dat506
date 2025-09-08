import sys
import wordfreq
import urllib.request



#argv[1] är det första man skriver in i cmd, dvs txtn som alla stoppord kommer stå i. 
#argv[2] ska vara txt som är exempelartiklarna bifogade, också txt
#argv[3] ska vara antal ord vi vill ha i listan räknade
def main():

    stoppord = wordfreq.tokenize([open(sys.argv[1]).read()])
    bulkText = wordfreq.tokenize([urllib.request.urlopen(sys.argv[2]).read().decode("utf-8")])
    antal = int(sys.argv[3])
    

    wordfreq.printTopMost(wordfreq.countWords(bulkText,stoppord),antal)

    #Vi ska få argv1 att bli en lista med stoppord, som ska infogas i CountWords, argv2 kommer vara texten som ska analyseras, alltså text.
    #arv3 kommer vara n 

main()
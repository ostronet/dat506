
import sys
import wordfreq
import urllib.request



#argv[1] är det första man skriver in i cmd, dvs txtn som alla stoppord kommer stå i. 
#argv[2] ska vara txt som är exempelartiklarna bifogade, också txt
#argv[3] ska vara antal ord vi vill ha i listan räknade
def main():

    urlCheck1 = ['h','t','t','p','s']
    urlCheck2 = ['h','t','t','p',':']
    urlTest = []
    for element in range (0,5):
        urlTest.append(sys.argv[2][element])

    if urlTest == urlCheck1 or urlTest == urlCheck2:

        bulkText = wordfreq.tokenize([urllib.request.urlopen(sys.argv[2]).read().decode("utf-8")])
    
    else:
        bulkText = wordfreq.tokenize([open(sys.argv[2]).read()])

    stoppord = wordfreq.tokenize([open(sys.argv[1]).read()])
    antal = int(sys.argv[3])
    

    wordfreq.printTopMost(wordfreq.countWords(bulkText,stoppord),antal)

    #Vi ska få argv1 att bli en lista med stoppord, som ska infogas i CountWords, argv2 kommer vara texten som ska analyseras, alltså text.
    #arv3 kommer vara n 

if "--help" in sys.argv:
    print("1: Fil för stoppord")
    print("2: Fil för bulktext")
    print("3: Antal ord som ska visas")
    sys.exit(0)

    
    
if __name__ == "__main__":
    main()

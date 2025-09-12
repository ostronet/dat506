
import sys
import wordfreq
import urllib.request


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


if "--help" in sys.argv:                #--help till för när vi testkörde koden och lätt glömde bort vad vilket argument som var vad. 
    print("arg1: Fil för stoppord")
    print("arg2: Fil för bulktext")
    print("arg3: Antal ord som ska visas")
    sys.exit(0)

    
    
if __name__ == "__main__":
    main()

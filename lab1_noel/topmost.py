import wordfreq as wf
import sys
import urllib.request

def main():
    stopp = open(sys.argv[1])
    response = urllib.request.urlopen(sys.argv[2])
    lines = response.read().decode("utf8").splitlines()
    response.close
    n=int(sys.argv[3])

    text_1 = wf.tokenize(lines)

    stopp_ = []
    for i in stopp:
        s = i.strip()
        if s != "":
            stopp_.append(s)
    stopp.close()

    antal = wf.countWords(text_1, stopp_)
    wf.printTopMost(antal, n)

main()






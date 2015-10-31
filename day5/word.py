import random


def wordlist():
    f = open("/usr/share/dict/words")
    clean_words = []
    for i in f :
        i = i.strip()
        if i.isalpha() and len(i) > 5 :
            clean_words.append(i.lower())
    return clean_words



def select(wordlist):
    return random.sample(wordlist,1)[0]



def game(word):

    error=0
    le = len(word)
    print " ua word is {}  10 Lives left".format("*"*len(word))
    list2=[]
    
    for x in word:
        list2.append("*")
        
    while error < 10:
        alpha=raw_input()
        
        if alpha in word:
            ind = [x for x in range(len(word)) if alpha == word[x]]
            for x in ind:
                list2[x]=alpha
        else:
            error=error+1
        
        print "ua  word = {}  {} Lives Left".format(''.join(list2),10-error)
        
        if error == 10 :
            print " {} Game Over {}".format(10*"%",10*"%")
        elif not("*" in list2):
             print " {} GOTCHA {}".format(10*"%",10*"%")
             error=11

        

        
            
    
if __name__ == "__main__":

    wordlist=wordlist()
    word=select(wordlist)
    game(word)


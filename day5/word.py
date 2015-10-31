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
    print " ua word is {}".format("*"*len(word))
    print word
    list2=[]
    for x in word:
        #list1.append(x)
        list2.append("*")
        
    for x in range(10):
        
        alpha=raw_input()
        if alpha in word:
            ind = [x for x in range(len(word)) if alpha == word[x]]
            for x in ind:
                list2[x]=alpha
            print ''.join(list2)
        else:
            error=error+1
            print "{}   {}".format(error,''.join(list2))


            
    


                
    
    


wordlist=wordlist()

word=select(wordlist)


game(word)


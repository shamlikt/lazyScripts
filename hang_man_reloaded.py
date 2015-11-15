import random

def get_secret_word():
    f = open("/usr/share/dict/words")
    clean_words = []
    for i in f :
        i = i.strip()
        if i.isalpha() and len(i) > 5 :
            clean_words.append(i.lower())
    return random.sample(clean_words,1)[0]


def check_game_over(secret,gussword,w_no):
   
    if ''.join(gussword) == secret:
        print "\t\tYOU WON"
        exit()
    elif w_no > 10:
        print "\t\tFAILED"
        print "\t Word is %s"%(secret)
        exit()


def output(guss_word,w_no):
    return " Word is {} \t chance left is {}".format(''.join(guss_word),10-w_no)


def get_input():
    return raw_input("Enter the alpha > :")



def update_word(s_word,p_word,w_no):
    guss = get_input()
    if guss in s_word:
            index = [x for x in range (len(s_word ))if guss == s_word[x]] #
            for x in index:
                   p_word[x] = guss
    else : 
            w_no = w_no+1
    return p_word,w_no




def main():
    print " WELCOME TO HANG_MAN GAME"
    s_word = get_secret_word()
    print output([x for x in "*"*len(s_word)],0)
    p_word = [x for x in "*" * len(s_word)]
    w_no = 0
    while True:
            p_word,w_no = update_word(s_word,p_word,w_no)
            print output(p_word,w_no) 
            check_game_over(s_word,p_word,w_no)


main()
        

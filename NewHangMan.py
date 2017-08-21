import random
import os
words = " moon word uber tiger elephant house mouse computer cartoon program character phone laptop ".lower().split()
def ranword():
    randword = words[random.randint(0,(len(words)-1))]
    return randword

def guess():
    while True:
        try:
            guesslet = raw_input("Guess the letter: ").lower()[0]
            break
        except IndexError:
            print "Oops, That was not valid letter"
    return guesslet

hangpic = ['''
    +-----+
          |
          |
          |
          |
  ===========        
''','''
    +-----+
    o     |
          |
          |
          |
  =========== 
''','''
    +-----+
    o     |
   /|     |
          |
          |
  =========== 
''','''
    +-----+
    o     |
   /|\    |
          |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
          |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
    |     |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
    |     |
     \    |
  ===========

''','''
    +-----+
    o     |
   /|\    |
    |     |
   / \    |
  ===========
'''
]
play = 'y'
while play == 'y':
    os.system('cls')
    guessed = ''
    missfire = 0
    win = 0
    missed = ''
    rankword = ranword()
    blanks = '_' * len(rankword)
    while True:
        print hangpic[missfire]
        print "Missed Letter: ", missed
        print "you have %s chance to go" % (7 - missfire)
        print blanks
        guesslet = guess()
        if guesslet not in 'abcdefghijklmnopqrstuvwxyz':
            print "please enter letter"
        elif guesslet in missed:
            print "You have already missed that letter"
        elif guesslet in guessed:
            print "you have already guessed that letter"
        elif guesslet in rankword:
            print "You have matched %s letter" %win
            win += 1
            guessed += guesslet
            man = list(blanks)
            blanks = ''
            i = rankword.find(guesslet)
            man[i] = guesslet
            for i in man:
                blanks = blanks + i
        else:
            print "you have missed the letter"
            missed += guesslet
            missfire += 1
        if win == len(rankword):
            print "you won the game"
            print rankword
            break
        if missfire == 7:
            print "you lose the game"
            print rankword
            break
    play = raw_input("Do you want to play it again(y): ")



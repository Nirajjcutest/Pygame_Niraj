import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'ant article  badger boat bat bear best camel cat clam cobra count cougar crow  dog dirt donkey duck fox frog fun goat girl hawk heavy lion lizard luck mole mute monkey mouse mule newt nice owl pigeon pot python ram rat raven rhino salmon seal shark  sloth snake spider stork swan tiger toad turkey whale wolf wombat zebra'.split()

def ranword():
    return words[random.randint(0,len(words)-1)]

def hangmanpic(missedletter,randomword):
    global missed
    global missletter
    global blanks
    global win
    global alreadyguess
    chance = 0
    #print guessletter
    print 'HANGMAN BROUGHT TO BY NIRAJ'
    print HANGMANPICS[missed]
    print 'Missed Letter: ' + missletter
    #print randomword
    print blanks
    guess()
    if guessletter in randomword:
        k = 0
        for i in randomword:
            if guessletter == i:
                t = k
            k += 1
        man = list(blanks)
        man[t] = guessletter
        blanks = ''
        for i in man:
            blanks += i 
        win += 1
        alreadyguess += guessletter
    else:
        missed += 1
        missletter += guessletter
        
def guess():
    global guessletter
    while True:
        guessletter = raw_input('Guess a letter: ')
        if len(guessletter) != 1:
            print 'Please Enter one letter'
        elif guessletter in missletter:
            print 'You have already missed the letter'
        elif guessletter in alreadyguess:
            print 'you have already guess the letter'
        elif guessletter not in 'abcdefghijklmnopqrstuvwxyz':
            print 'Please Enter a letter'
        else:
            return guessletter
    
userdemand = 'yes'
while userdemand == 'yes' or userdemand == 'y':
    
    rankword = ranword()
    missed = 0
    missletter = ''
    alreadyguess = ''
    win = 0
    blanks = '-'*len(rankword)
    while missed <= 6:
        hangmanpic(missed,rankword)
        if win == len(rankword):
            print 'you win'
            print rankword
            break
    if missed == 7:
        print 'Game Over'
        print rankword
    userdemand = raw_input("Play Again(yes/y): ")




    



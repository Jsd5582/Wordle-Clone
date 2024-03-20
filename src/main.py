#!/usr/bin/env python

import random

"""
Note to self: Running into a bug where letters arent being removed from the Available letters list even if they aren't in the answer word. Check the loop in lines 23-29.
"""


'''Global variables'''
Available_Letters = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
WORD_LIST = ['Tiger','Cloud', 'Ocean', 'Chair', 'Ghost', 'Knife', 'Mouse', 'Plant', 'Queen', 'Radar', 'Stone', 'Brush', 'Apple',
            'Toast', 'Wagon', 'Llama', 'House', 'Clown', 'Crane', 'Flame']
LIVES = 5

def shared_letters(user_word, actual_word, unavailable_letters) -> list:
    cap_word = user_word.upper()
    guess = [*cap_word]
    answer = [*actual_word]
    unavailable = [*unavailable_letters]
    shared = []

    for i in range(len(answer)):
        '''If the elements match they are added to the list named shared'''
        if guess[i] == answer[i]:
            shared.append(answer[i])
        else:
            unavailable.remove(guess[i])
            shared.append('-')

    return shared,unavailable

def wordle(word):

    '''Just a place holder to see the picked word to ensure that the algorithm is preforming as intended'''
    print(word)

    for i in range(LIVES):
        show, new_avail = shared_letters('house',word, Available_Letters)
        print(show)
        print(new_avail)        

def word_picker() -> str:
    '''
    Purpose: Pick a word within the list based on the index randomizer from the first index to the last to capture all elements
    Args:
        none
    
    Return:
        The randomly picked word from the list of available words
    '''
    max = len(WORD_LIST)
    word = WORD_LIST[random.randint(0,max)]
    
    """Word is returned capitalized to ensure that capitalization from the user is not a facotr in whether the systemm determines if the input is correct for not"""
    return word.upper()

def main():
    print ("All available letters are: " + Available_Letters)
    picked_word = word_picker() 
    wordle( picked_word )

if __name__ == '__main__':
    main()
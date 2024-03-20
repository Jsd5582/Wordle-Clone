#!/usr/bin/env python

import random

"""
Note to self: Running into a bug where letters arent being removed from the Available letters list even if they aren't in the answer word. Check the loop in lines 23-29.
"""


'''Global variables'''
WORD_LIST = ['Tiger','Cloud', 'Ocean', 'Chair', 'Ghost', 'Knife', 'Mouse', 'Plant', 'Queen', 'Radar', 'Stone', 'Brush', 'Apple',
            'Toast', 'Wagon', 'Llama', 'House', 'Clown', 'Crane', 'Flame']
LIVES = 5

def remove_irrelevant_letters(useless_letters, all_letters) -> list:
    for i in useless_letters[:]:
        if i in all_letters:
            all_letters.remove(i)
    
    return all_letters

def shared_letters(user_word, actual_word) -> list:
    guess = [*user_word]
    answer = [*actual_word]
    unavailable = []
    shared = []

    for i in range(len(answer)):
        '''If the elements match they are added to the list named shared'''
        if guess[i] == answer[i]:
            shared.append(answer[i])
        elif guess[i] != answer[i]:
            unavailable.append(answer[i])
            shared.append('-')

    return shared,unavailable

def wordle(word, letters):

    '''Just a place holder to see the picked word to ensure that the algorithm is preforming as intended'''
    print(word)

    for i in range(LIVES):
        show, new_avail = shared_letters('HOUSE',word)
        print(show)
        new_avail = remove_irrelevant_letters(new_avail, letters)
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
    Available_Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','W','Y','Z']
    print ("All available letters are: ")
    print(*Available_Letters, sep = ", ")
    picked_word = word_picker() 
    wordle( picked_word, Available_Letters )

if __name__ == '__main__':
    main()
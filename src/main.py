#!/usr/bin/env python

import random


'''Global variables'''
AVAILABLE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
unavailable_letters = ''
WORD_LIST = ['Tiger','Cloud', 'Ocean', 'Chair', 'Ghost', 'Knife', 'Mouse', 'Plant', 'Queen', 'Radar', 'Stone', 'Brush', 'Apple',
            'Toast', 'Wagon', 'Llama', 'House', 'Clown', 'Crane', 'Flame']
LIVES = 5

def shared_letters(user_word, actual_word, unavailable_letters) -> list:
    guess = [*user_word]
    answer = [*actual_word]
    shared = []

    for i in range(len(answer)):
        if guess[i] == answer[i]:
            shared.append(answer[i])
        else:
            unavailable_letters = unavailable_letters + guess[i].upper()

    return shared

def wordle(word):
    unavailable_letters = ''
    for i in range(LIVES):
        print(shared_letters('house',word, unavailable_letters))
        

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

    return word

def main():
    print (AVAILABLE_LETTERS)
    print ( word_picker() )
    wordle( word_picker() )

if __name__ == '__main__':
    main()
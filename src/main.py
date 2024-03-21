#!/usr/bin/env python

import random



'''Global variables'''
WORD_LIST = ['Tiger','Cloud', 'Ocean', 'Chair', 'Ghost', 'Knife', 'Mouse', 'Plant', 'Queen', 'Radar', 'Stone', 'Brush', 'Apple',
            'Toast', 'Wagon', 'Llama', 'House', 'Clown', 'Crane', 'Flame']
LIVES = 5

def remove_irrelevant_letters(useless_letters, all_letters) -> list:
    """
    Purpose: Remove all the unused letters collected in the useless_letters list from the all_letters list
             to keep trace of all the relavent letters

    Args:
        useless_letters: A list of letters used from the users latest guess that are not in the answer word
        all_letters: A list of all the letters that can still be used to form a guess

    Return:
        An updated list of all the letters that the user can still use
    """

    for i in useless_letters[:]:
        if i in all_letters:
            all_letters.remove(i)
    
    return all_letters

def shared_letters(user_word, actual_word) -> list:
    """
    Purpose: Determine the shared letters between the word guessed by the user and the actual word

    Args:
        user_word: The word that the user guessed
        actual_word: The actual answer word
    
    Return:
        shared: A list of all the shared between the user entered word and the answer
        unavailable: A list of all the letters from the user word that is not in the answer
    """

    guess = [*user_word]
    answer = [*actual_word]
    unavailable = []
    shared = []

    for i in range(len(answer)):
        # If both letters are the same at the same index
        if guess[i] == answer[i]:
            shared.append(answer[i])
        # If the letter in the guess word exists within the answer
        elif guess[i] in answer:
            shared.append('-')
        # If the letter in the guess would isn't in the answer at all
        elif guess[i] not in answer[i]:
            unavailable.append(guess[i])
            shared.append('-')

    return shared,unavailable

def wordle(actual_word,letters):
    """
    Purpose: The main program of the game

    Args:
        actual_word: The answer word
        user_word: The guessed word
        letters: A list of available letters
    
    Return:
        None
    """

    '''Just a place holder to see the picked word to ensure that the algorithm is preforming as intended'''
    print(actual_word)

    for i in range(LIVES):
        user_word = input("Enter a word: ")
        show, new_avail = shared_letters(user_word,actual_word)
        print(show)
        new_avail = remove_irrelevant_letters(new_avail, letters)
        print(new_avail)
        guess_str = ''.join(show)
        if actual_word == guess_str:
            print("Winner")
            break


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
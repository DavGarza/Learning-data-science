import random
import os


print("""
These are the difficulties
1- Easy
2- Medium
3- Hard
""")


def run():
    
    dif = int(input("Choose your difficulty"))
    words = []

    if dif == 1:
        with open("/home/david_gza/Archivos/data_science/git/python_projects/intermidiate_python/file_to_operate/easy_level.txt") as x:
            for line in x:
                words.append(line.strip().upper())
    if dif == 2:
        with open("/home/david_gza/Archivos/data_science/git/python_projects/intermidiate_python/file_to_operate/medium_level.txt") as x:
            for line in x:
                words.append(line.strip().upper())
    if dif == 3:
        with open("/home/david_gza/Archivos/data_science/git/python_projects/intermidiate_python/file_to_operate/hard_level.txt") as x:
            for line in x:
                words.append(line.strip().upper())
    
    word_to_guess = random.choice(words)
    word_hided = "-" * len(word_to_guess)
    word_hided_list = list(word_hided)
    lifes = 6
    print("Start!, you have", lifes, "lifes")
    win = False
    guessed_letters = []
    letters_in_word = [letter for letter in word_to_guess]
    while win == False and lifes > 0:
        print(word_hided)
        print("You have", lifes, "left")
        guess = input("Enter a letter").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already enter", guess)
            elif guess not in letters_in_word:
                print(guess, "Not in the words")
                lifes -= 1
                guessed_letters.append(guess)
            else:
                print(guess, "is correct")
                guessed_letters.append(guess)
                indices = [i for i, letter in enumerate(word_to_guess) if letter == guess]
                for index in indices:
                    word_hided_list[index] = guess
                word_hided = "".join(word_hided_list)
                if "-" not in word_hided:
                    win = True
        else:
            print("Enter only 1 letter")
    if win == True:
        print("Great you´ve won! :)")
    else:
        print("You´ve lose :( the word was", word_to_guess)

if __name__ == "__main__":
    run()
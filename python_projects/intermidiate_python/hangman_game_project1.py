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
    lifes = 6
    print("Start!, you have", lifes, "lifes")



if __name__ == "__main__":
    run()
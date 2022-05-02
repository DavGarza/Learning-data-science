import random

def lenght(func):
    def counting(message: str):
        message = int(len(message))
    return counting

words = ["Airplane", "Node", "Intrinsic", "System", "Power", "Evolution"]

@lenght
def get_word():
    word = random.choice(words)
    return word

def run():
    print(get_word)



if __name__ == "__main__":
    run()
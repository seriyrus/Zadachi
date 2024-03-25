from random import choice as c


bad_words = ['дегенерат','придурок','инвалид','недоразвитый']

good_words = ["просто хороший человек","доразвитый",
              "ergweg","swfwf"]


def r_good():
    return c(good_words)

def r_bad():
    return c(bad_words)


def main():

    print("Привет! Как тебя зовут?")
    name = input()

    if name == "q":
        exit()

    v = input("Хочешь доброго кузю?[да]: ")
    if v.lower() == 'да' or "y":
        phrase = r_good()
    else:
        phrase = r_bad()

    print(f"Привет {name}! ты выглядишь сегодня как {phrase}!")

    


if __name__ == "__main__":
    while True:
        main()
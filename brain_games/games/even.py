from random import randint
from ..engine import run_engine

def is_even(num):
    return num % 2 == 0


def generate_round():
    question = randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'

    return (question, answer)


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_engine(rules, generate_round)

if __name__ == "__main__":
    main()
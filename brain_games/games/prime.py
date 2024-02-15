from random import randint
from ..engine import run_engine


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, (num // 2) + 1):
        print(i)
        if num % i == 0:
            return False
    return True

def generate_round():
    number = randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    question = str(number)

    return (question, answer)


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_engine(rules, generate_round)
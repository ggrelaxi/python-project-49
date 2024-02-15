from random import randint
from ..engine import run_engine


def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))

    return (question, answer)


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    run_engine(rules, generate_round)

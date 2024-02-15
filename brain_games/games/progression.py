from random import randint
from ..engine import run_engine


def generate_progression(start, step, length):
    progression = []

    for i in range(length):
        progression.append(start + step * i)

    return progression


def generate_round():
    start = randint(0, 10)
    step = randint(5, 10)
    length = 10

    progression = generate_progression(start, step, length)

    hidden_index = randint(0, length - 1)

    answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return (question, answer)


def main():
    rules = 'What number is missing in the progression?'
    run_engine(rules, generate_round)

from random import randrange, randint
from ..engine import run_engine


def get_random_operator():
    operators = ['+', '-', '*']
    return operators[randrange(0, len(operators))]


def calculate(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise TypeError(f'Invalid operator - {operator}')


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = get_random_operator()
    question = f'{num1} {operator} {num2}'
    answer = str(calculate(num1, num2, operator))

    return (question, answer)


def main():
    rules = 'What is the result of the expression?'
    run_engine(rules, generate_round)


if __name__ == '__main__':
    main()

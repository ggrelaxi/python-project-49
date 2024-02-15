import prompt


ROUNDS_COUNT = 3


def run_engine(rules, generateRound):
    print('Welcome to the Brain Games!')
    print(rules)

    name = prompt.string('May i Have your name? ')

    print(f'Hello, {name}')

    for i in range(ROUNDS_COUNT):
        question, corrent_answer = generateRound()

        print('Question:', question)
        user_answer = prompt.string('Your answer: ')

        if user_answer != corrent_answer:
            print(f'{user_answer} is wrong answer ;(. ')
            print(f'Correct answer was {corrent_answer}.')
            print(f"Let's try again, {name}")
            return

        print('Correct')

    print(f'Congratulations, {name}!')

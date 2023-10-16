#!/usr/bin/env python3
import random

import prompt

from brain_games.cli import welcome_user

from brain_games.scripts.brain_games import greet


def even_or_odd():
    name = welcome_user()
    counter = 0
    correct_ans = ''
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while counter < 3:
        num = random.randint(1, 100)
        correct_ans = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_ans:
            print('Correct!')
            counter += 1
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_ans}".'
                  f'\nLet\'s try again!')
            break
    if counter == 3:
        print(f'Congratulation, {name}!')


def main():
    greet()
    even_or_odd()

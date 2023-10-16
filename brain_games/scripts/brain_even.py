#!/usr/bin/env python3
import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet

NUM_QUESTIONS = 3


def ask_question_and_check_answer():
    num = random.randint(1, 100)
    correct_ans = 'yes' if num % 2 == 0 else 'no'
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    if answer.lower() == correct_ans:
        print('Correct!')
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_ans}".'
              f'\nLet\'s try again!')
        return False


def even_or_odd():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for _ in range(NUM_QUESTIONS):
        if not ask_question_and_check_answer():
            return
    print(f'Congratulation, {name}!')


def main():
    greet()
    even_or_odd()

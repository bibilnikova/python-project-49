#!/usr/bin/env python3
import prompt
from ..cli import welcome_user


def ask_question_and_check_answer(question, correct_ans, answer_type):
    print(question)
    if answer_type == 'integer':
        answer = prompt.integer('Your answer: ')
    elif answer_type == 'string':
        answer = prompt.string('Your answer: ')
    if answer == correct_ans:
        print('Correct!')
        return True
    else:
        print(f'"{answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_ans}".'
              f'\nLet\'s try again!')
        return False


def game_loop(game, sentance, ans_type):
    name = welcome_user()
    print(sentance)
    for _ in range(3):
        question, correct_ans = game()
        if not ask_question_and_check_answer(question, correct_ans, ans_type):
            return
    print(f'Congratulations, {name}!')


def main():
    game_loop()


if __name__ == "__main__":
    main()

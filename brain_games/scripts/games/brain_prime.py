#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import greet
from ..game_logic import game_loop


def prime():
    num = random.randint(1, 100)
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                correct_ans = 'no'
                break
        else:
            correct_ans = 'yes'
    else:
        correct_ans = 'no'
    question = f'Question: {num}'
    return question, correct_ans


def play():
    sentance = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    ans_type = 'string'
    return game_loop(prime, sentance, ans_type)


def main():
    greet()
    play()

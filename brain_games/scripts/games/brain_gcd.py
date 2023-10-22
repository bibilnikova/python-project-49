#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import greet
from ..game_logic import game_loop


def gcd():
    num1, num2 = random.randint(1, 50), random.randint(1, 50)
    question = f'Question: {num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    correct_ans = num1 + num2
    return question, correct_ans


def play():
    sentance = 'Find the greatest common divisor of given numbers.'
    ans_type = 'integer'
    return game_loop(gcd, sentance, ans_type)


def main():
    greet()
    play()

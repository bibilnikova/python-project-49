#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import greet
from ..game_logic import game_loop


def even_or_odd():
    num = random.randint(1, 100)
    correct_ans = 'yes' if num % 2 == 0 else 'no'
    question = f'Question: {num}'
    return question, correct_ans


def play():
    sentance = 'Answer "yes" if the number is even, otherwise answer "no".'
    ans_type = 'string'
    return game_loop(even_or_odd, sentance, ans_type)


def main():
    greet()
    play()

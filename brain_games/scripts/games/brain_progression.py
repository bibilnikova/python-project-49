#!/usr/bin/env python3
import random
from brain_games.scripts.brain_games import greet
from ..game_logic import game_loop


def progression():
    length_progression = random.randint(5, 10)
    first_num = random.randint(1, 20)
    step = random.randint(1, 9)
    arr = []
    for i in range(length_progression + 1):
        if i != 0:
            first_num += step
        else:
            first_num += i
        arr.append(first_num)
    rand_index = random.randint(0, len(arr) - 1)
    correct_ans = arr[rand_index]
    arr[rand_index] = '..'
    question = f'Question: {" ".join(map(str, arr))}'
    return question, correct_ans


def play():
    sentance = 'What number is missing in the progression?'
    ans_type = 'integer'
    return game_loop(progression, sentance, ans_type)


def main():
    greet()
    play()

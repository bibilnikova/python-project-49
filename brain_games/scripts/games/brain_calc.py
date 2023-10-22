import random
from brain_games.scripts.brain_games import greet
from ..game_logic import game_loop


def calculation():
    num1, num2 = random.randint(1, 50), random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    question = f'Question: {num1} {operator} {num2}'
    match operator:
        case '+':
            correct_ans = num1 + num2
        case '-':
            correct_ans = num1 - num2
        case '*':
            correct_ans = num1 * num2
    return question, correct_ans


def play():
    sentance = 'What is the result of the expression?'
    ans_type = 'integer'
    return game_loop(calculation, sentance, ans_type)


def main():
    greet()
    play()

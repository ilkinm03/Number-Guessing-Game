from random import randint
import os
from difficulty_levels import DIFFICULTY


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
        return -1
    elif guess < answer:
        print("Too low")
        return -1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0


def choose_diffulty():
    choice = input("Choose a difficulty level: easy, medium or hard? ").lower()
    if choice not in DIFFICULTY:
        return choose_diffulty()
    return choice


def choose_number():
    guess = int(input("Guess a number: "))
    if guess > 100 or guess < 1:
        return choose_number()
    return guess


def start_game():
    clear_screen()
    answer = randint(1, 100)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking a number between 1 and 100")
    choice = choose_diffulty()
    lifes = DIFFICULTY[choice]
    clear_screen()
    while lifes:
        print(f"Lifes: {lifes}")
        guess = choose_number()
        clear_screen()
        is_life = check_answer(guess, answer)
        if is_life == 0:
            break
        lifes += is_life
    clear_screen()
    if lifes == 0:
        print(f"You lose. The answer was {answer}.")


start_game()

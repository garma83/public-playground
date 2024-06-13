import random
import os
import argparse
from colorama import Fore, Style

def main(tafel):
    os.system('clear')
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        answer = input(f"Wat is {a} x {tafel}? ")
        os.system('clear')
        if answer == str(a * tafel):
            print(f"{Fore.GREEN}Heel goed! :) {a} x {tafel} is inderdaad {a * tafel}.{Style.RESET_ALL}")
            score += 1
        else:
            print(f"{Fore.RED}Helaas... Het goede antwoord is {a * tafel}.{Style.RESET_ALL}")
    print(f"Van de 10 vragen heb je er {score} goed.")
    with open("scores.txt", "a") as file:
        file.write(f"Score voor tafel {tafel}: {score}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tafel", type=int, help="The multiplier for the multiplication table")
    args = parser.parse_args()
    main(args.tafel)
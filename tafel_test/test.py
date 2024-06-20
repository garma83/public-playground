import random
import os
import argparse
from colorama import Fore, Style

def main(tafel):
    if tafel == 'scores':
        with open("scores.txt", "r") as file:
            print(file.read())
    else:
        tafel = int(tafel)
        os.system('clear')
        score = 0
        for i in range(10):
            a = random.randint(1, 10)
            answer = input(f"Vraag {i+1}: Wat is {a} x {tafel}? ")
            os.system('clear')
            if answer == str(a * tafel):
                print(f"{Fore.GREEN}Heel goed! :) {a} x {tafel} is inderdaad {a * tafel}.{Style.RESET_ALL}")
                score += 1
            else:
                print(f"{Fore.RED}Helaas... Het goede antwoord is {a * tafel}.{Style.RESET_ALL}. Je had ingetypt: '{answer}'")
        print(f"Van de 10 vragen heb je er {score} goed.")
        with open("scores.txt", "a") as file:
            file.write(f"Score voor tafel {tafel}: {score}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tafel", help="The multiplier for the multiplication table or 'scores' to print scores")
    args = parser.parse_args()
    main(args.tafel)
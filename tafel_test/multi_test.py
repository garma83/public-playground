import random
import os
import argparse
from colorama import Fore, Style

def main(tafels):

    os.system('clear')

    nrquestions = 20

    score = 0
    for i in range(nrquestions):
        tafel = random.choice(tafels)
        a = random.randint(1, 10)
        answer = input(f"Vraag {i+1}: Wat is {a} x {tafel}? ")
        os.system('clear')
        if answer == str(a * tafel):
            print(f"{Fore.GREEN}Heel goed! :) {a} x {tafel} is inderdaad {a * tafel}.{Style.RESET_ALL}")
            score += 1
        else:
            print(f"{Fore.RED}Helaas... Het goede antwoord is {a * tafel}.{Style.RESET_ALL}. Je had ingetypt: '{answer}'")
    print(f"Van de {nrquestions} vragen heb je er {score} goed.")
    with open("scores.txt", "a") as file:
        tafels_str = ", ".join([str(tafel) for tafel in tafels])
        file.write(f"Score voor tafels {tafels_str}: {score} van {nrquestions}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('tafels', metavar='N', nargs='+', help='De tafels die geoefend moeten worden')
    args = parser.parse_args()

    if args.tafels[0] == 'scores':
        with open("scores.txt", "r") as file:
            print(file.read())
            
    else:
        tafels = [int(tafel) for tafel in args.tafels]
        main(tafels)
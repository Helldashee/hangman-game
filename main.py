import random
from wordslist import words

hangman_art = {0: ("  ",
                   "  ",
                   "  "
                   ),
               1: (" 0 ",
                   "  ",
                   "  "),
               2: (" 0 ",
                   " | ",
                   "  "),
               3: (" 0 ",
                   "/| ",
                   "  "),
               4: (" 0 ",
                   "/|\\",
                   "  "),
               5: (" 0 ",
                   "/|\\",
                   "/ "),
               6: (" 0 ",
                   "/|\\",
                   "/ \\"),}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    clue_count = 0
    guessed_letters = set()
    guessed_words = set()
    is_running = True
    is_running_difficulty = True

    while is_running_difficulty:
        difficulty = input("Choose difficulty level (1, 2, 3): ")
        if difficulty not in ("1", "2", "3"):
            print("Invalid input")
            continue

        else:
            difficulty = int(difficulty)

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            if clue_count < 3:
                print(f"You have {3 - clue_count} clues")
                run_clue = input("Want to take clue? (y/n): ").lower()
                if len(run_clue) > 1 or run_clue.isdigit():
                    print("Invalid input")
                    continue
                elif run_clue not in ("y", "n"):
                    print("Invalid input")
                    continue
                elif run_clue == "y":
                    for i in range(len(answer)):
                        if hint[i] == "_":
                            hint[i] = answer[i]
                            display_hint(hint)
                            clue_count += 1
                            break

                else:
                    pass

            else:
                print("You don't have clues")

            choose_type = input("Choose type of answer - letter or word (l/w): ").lower()
            if len(choose_type) > 1 or choose_type.isdigit():
                print("Invalid input")
                continue

            elif choose_type == "l":
                guess = input("Enter a letter: ").lower()

                if len (guess) != 1 or not guess.isalpha():
                    print("Invalid input")
                    continue

                if guess in guessed_letters:
                    print(f"{guess} is already guessed")
                    continue

                guessed_letters.add(guess)

                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            hint[i] = guess
                else:
                    wrong_guesses += difficulty

            elif choose_type == "w":
                guess = input("Enter a word: ").lower()

                if len(guess) <= 1 or not guess.isalpha():
                    print("Invalid input")
                    continue

                if guess in guessed_words:
                    print(f"{guess} is already guessed")
                    continue

                guessed_words.add(guess)

                if guess == answer:
                    display_man(wrong_guesses)
                    display_answer(answer)
                    print("You win!")
                    is_running = False
                    is_running_difficulty = False

                else:
                    wrong_guesses += difficulty
            else:
                continue

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You win!")
                is_running = False
                is_running_difficulty = False

            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("You lose :(")
                is_running = False
                is_running_difficulty = False


if __name__ == "__main__":
    main()
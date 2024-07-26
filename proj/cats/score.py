import cats
import pickle
import time
import random

if __name__ == '__main__':
    pickled_file = "data/testcases.out"
    word_list = "data/final_diff_words.txt"

    with open(pickled_file.strip(), 'rb') as pickled_dict:
        test_dict = pickle.load(pickled_dict)

    with open(word_list.strip(), 'r', encoding='utf8') as correct_file:
        correct_words = list(correct_file.read().split())

    start_time = time.time()

    correct_words = list(test_dict.keys())
    random.shuffle(correct_words)
    correctly_corrected, incorrectly_corrected, not_corrected, trial_counter = 0, 0, 0, 0
    for correct in correct_words:
        elapsed_time = time.time() - start_time
        if elapsed_time > 45:
            break
        typos = test_dict[correct]
        for_print = f"{correct}\n"
        for typo in typos:
            guess = cats.autocorrect(typo, correct_words, cats.final_diff, cats.FINAL_DIFF_LIMIT)
            if guess == correct:
                for_print += f"\tCorrect: ({typo} -> {guess})\n"
                correctly_corrected += 1
            elif guess != typo:
                for_print += f"\tIncorrect: ({typo} -> {guess})\n"
                incorrectly_corrected += 1
            else:
                for_print += f"\tNo change: ({typo} -> {typo})\n"
                not_corrected += 1
            trial_counter += 1
        print(for_print)

    print(f"Correction Speed: {(trial_counter / elapsed_time) * 60} wpm")
    print(f"Correctly Corrected: {correctly_corrected} words")
    print(f"Incorrectly Corrected: {incorrectly_corrected} words")
    print(f"Uncorrected: {not_corrected} words")
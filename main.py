import argparse
from collections import Counter

from app.random_number_generator import RandomNumberGenerator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--numbers",
        nargs="+",
        required=True,
        type=int,
        help="Numbers to sample from.",
    )
    parser.add_argument(
        "-p",
        "--probabilities",
        nargs="+",
        required=True,
        type=float,
        help="Discrete probabilities for sampling.",
    )
    parser.add_argument("-r", "--runs", type=int, required=True, help="Number of runs.")
    args = parser.parse_args()

    random_number_generator = RandomNumberGenerator(args.numbers, args.probabilities)
    samples_counter = Counter(random_number_generator.sample_k(args.runs))

    print(f"--- Results from the experiment ---")
    for number in random_number_generator.numbers:
        print(f"Number {number} drawn {samples_counter[number]} times.")

import random
from bisect import bisect
from itertools import accumulate
from typing import Any

from app.exceptions import (
    EmptyInput,
    InvalidProbability,
    NumbersAndProbabilitiesLengthMismatch,
    InvalidProbabilitiesSum,
    InvalidNumberOfRuns,
)


class RandomNumberGenerator:
    def __init__(self, numbers: list[int], probabilities: list[float]):
        self.__validate_input(numbers, probabilities)
        self.numbers = numbers
        self.cumulative_probabilities = list(accumulate(probabilities))

    @staticmethod
    def __validate_input(numbers: list[Any], probabilities: list[float]) -> None:
        if not numbers or not probabilities:
            raise EmptyInput(f"Numbers/probabilities cannot be empty lists.")

        if [prob for prob in probabilities if prob <= 0 or prob > 1]:
            raise InvalidProbability(
                f"Probabilities should be positive numbers less than 1."
            )

        sum_of_probabilities = sum(probabilities)
        if sum_of_probabilities != 1:
            raise InvalidProbabilitiesSum(
                f"Invalid probability list provided. The probabilities should sum to 1, but they sum to {sum_of_probabilities}."
            )

        if len(numbers) != len(probabilities):
            raise NumbersAndProbabilitiesLengthMismatch(
                f"The length of the list of numbers and the list of probabilities should be the same. "
                f"The provided input has {len(numbers)} numbers and {len(probabilities)} probabilities."
            )

    def sample(self):
        random_value = random.random()
        bisect_index = bisect(self.cumulative_probabilities, random_value)
        return self.numbers[bisect_index]

    def sample_k(self, k):
        if k < 0:
            raise InvalidNumberOfRuns("Number of runs has to be a number greater than 0.")
        return [self.sample() for _ in range(k)]

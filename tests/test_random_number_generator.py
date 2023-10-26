import random
from collections import Counter

import pytest

from app.exceptions import (
    EmptyInput,
    InvalidProbability,
    NumbersAndProbabilitiesLengthMismatch,
    InvalidProbabilitiesSum,
    InvalidNumberOfRuns,
)
from app.random_number_generator import RandomNumberGenerator

SEED = 10


def seed(func):
    def wrapper(*args, **kwargs):
        random.seed(10)
        func(*args, **kwargs)
        random.seed(None)

    return wrapper


def test_empty_list_input():
    with pytest.raises(EmptyInput):
        RandomNumberGenerator(numbers=[], probabilities=[])


def test_invalid_probabilities_sum():
    with pytest.raises(InvalidProbabilitiesSum):
        RandomNumberGenerator(numbers=[1, 2, 3], probabilities=[0.5, 0.5, 0.7])


def test_length_of_numbers_and_probabilities_mismatch():
    with pytest.raises(NumbersAndProbabilitiesLengthMismatch):
        RandomNumberGenerator(numbers=[1, 2, 3], probabilities=[0.5, 0.5])


def test_zero_probability():
    with pytest.raises(InvalidProbability):
        RandomNumberGenerator(numbers=[1, 2, 3], probabilities=[0.5, 0.5, 0])


def test_negative_probability():
    with pytest.raises(InvalidProbability):
        RandomNumberGenerator(numbers=[1, 2, 3], probabilities=[-0.5, 0.5, 1])


def test_probability_grater_than_one():
    with pytest.raises(InvalidProbability):
        RandomNumberGenerator(numbers=[1, 2, 3], probabilities=[0.5, 0.1, 1.5])


def test_invalid_numer_of_runs():
    with pytest.raises(InvalidNumberOfRuns):
        generator = RandomNumberGenerator(
            numbers=[1, 2, 3], probabilities=[0.5, 0.4, 0.1]
        )
        generator.sample_k(-5)


@seed
def test_number_generator_with_seed_single_number():
    generator = RandomNumberGenerator(numbers=[8, 3, 1], probabilities=[0.6, 0.3, 0.1])
    number = generator.sample()
    assert number == 8


@seed
def test_number_generator_with_seed_multiple_numbers():
    generator = RandomNumberGenerator(numbers=[8, 3, 1], probabilities=[0.6, 0.3, 0.1])
    counter_samples = Counter(generator.sample_k(1000))
    assert counter_samples[8] == 595
    assert counter_samples[3] == 319
    assert counter_samples[1] == 86

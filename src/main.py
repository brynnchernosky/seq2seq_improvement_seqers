import numpy as np
import tensorflow as tf
import sys

from src.model import Seq2Seq
from src.preprocess import get_data, FRENCH_WINDOW_SIZE, ENGLISH_WINDOW_SIZE


def train(model, train_french, train_english, eng_padding_index):
    """
    Runs through one epoch - all training examples.
    :param model: the initialized model to use for forward and backward pass
    :param train_french: french train data (all data for training) of shape (num_sentences, 14)
    :param train_english: english train data (all data for training) of shape (num_sentences, 15)
    :param eng_padding_index: the padding index, the id of *PAD* token. This integer is used when masking padding labels.
    :return: None
    """
    pass


def test(model, test_french, test_english, eng_padding_index):
    """
    Runs through one epoch - all testing examples.
    :param model: the initialized model to use for forward and backward pass
    :param test_french: french test data (all data for testing) of shape (num_sentences, 14)
    :param test_english: english test data (all data for testing) of shape (num_sentences, 15)
    :param eng_padding_index: the padding index, the id of *PAD* token. This integer is used when masking padding labels.
    :returns: a tuple containing at index 0 the perplexity of the test set and at index 1 the per symbol accuracy on test set,
    e.g. (my_perplexity, my_accuracy)
    """

    return None, None


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"RNN", "ENHANCED"}:
        print("USAGE: python main.py <Model Type>")
        print("<Model Type>: [RNN/ENHANCED]")
        exit()

    train_english, test_english, train_french, test_french, \
        english_vocab, french_vocab, eng_padding_index = get_data(
            '../data/fls.txt', '../data/els.txt', '../data/flt.txt', '../data/elt.txt')

    model_args = (FRENCH_WINDOW_SIZE, len(french_vocab), ENGLISH_WINDOW_SIZE, len(english_vocab))

    if sys.argv[1] == "RNN":
        model = None
    else:
        model = Seq2Seq(*model_args)

    train(model, train_french, train_english, eng_padding_index)


if __name__ == '__main__':
    main()

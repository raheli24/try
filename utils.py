import random

import requests

from basic_word import BasicWord


def load_json_from_url(path):
    """
    Загружает данные по ссылке и возвращает их в виде списка или словаря,
    :param path: путь к источнику данных
    :return:
    """

    raw_data = requests.get(path)
    data = raw_data.json()
    return data


def load_random_word(path):
    """
    Возвращает случайное слово и его подслова в виде экземпляра класса BasicWord
    :param path: путь к источнику данных
    :return: экземпляр класса BasicWord
    """

    all_words = load_json_from_url(path)
    one_word = random.choice(all_words)
    word = one_word["word"]
    sub_words = one_word["subwords"]

    basic_word = BasicWord(word, sub_words)

    return basic_word




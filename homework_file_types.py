import json
from pprint import pprint
# алгоритм для json
# взять все description, оставить только длинные слова длиной больше 6 символов
# посчитать, сколько раз встречается слово в получившемся тексте
# оставить топ-10
# В решении домашнего задания вам могут помочь: split(), sort или sorted.
def split():
    result = []
    with open("files/newsafr.json", encoding="utf-8") as f:
        data = json.load(f)
        for news in data['rss']['channel']['items']:
            word = news['description'].upper().split()
            result.extend(word)
        return result

def count_and_sort(word):
    min_length = 6
    longer_words_list = []
    for good_words in word:
        if len(good_words) >= min_length:
            longer_words_list.append(good_words)

    longer_words_list.sort(key=longer_words_list.count, reverse=True)
    for i, words in enumerate(longer_words_list[0:10]):
        print(f'Слово "{words}" занимает {i + 1} место в топ-10 самых часто встречающихся в новостях слов.')

count_and_sort(split())



# алгоритм для hml
import xml.etree.ElementTree as ET

def count_and_sort(word):
    min_length = 6
    longer_words_list = []
    for good_words in word:
        if len(good_words) >= min_length:
            longer_words_list.append(good_words)

    longer_words_list.sort(key=longer_words_list.count, reverse=True)
    for i, words in enumerate(longer_words_list[0:10]):
        print(f'Слово "{words}" занимает {i + 1} место в топ-10 самых часто встречающихся в новостях слов.')

def split_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")
    for item in xml_items:
        word = item.find("description").text.upper().split()
    return word

count_and_sort(split_xml())
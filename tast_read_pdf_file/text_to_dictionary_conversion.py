from collections import OrderedDict


def get_dictionary(text):
    """
    Этот метод преобразует полученный текст в словарь
    :param text: получает текст после считывания информации из РDF-файла
    :return: словарь
    """
    lines = text.strip().split("\n")
    company_name = {"company_name": lines[0]}
    index = lines.index("NOTES:")
    main_dict = lines[1:index]
    notes = lines[index:]
    dict_notes = modify_notes(notes)
    dictionary = OrderedDict()
    dictionary.update(company_name)
    for line in main_dict:
        if ":" in line:
            key, value = line.split(":")
            dictionary.update({key.strip(): value.strip()})
    dictionary.update(dict_notes)
    return dictionary


def modify_notes(notes):
    """
    Этот метод получает заметки
    Этот метод написан дополнительно, потому что заметки приходят в разных строках
    :param notes: заметки в виде списка
    :return: словарь
    """
    key = notes[0].strip(":")
    value = notes[1:]
    dct = {key: value}
    return dct

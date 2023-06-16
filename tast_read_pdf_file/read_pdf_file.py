import os
from pprint import pprint
import fitz
from tast_read_pdf_file.text_to_dictionary_conversion import get_dictionary
from tast_read_pdf_file.test_data import data_to_verify


def get_file_path():
    """
    Этот метод получает абсолютный путь к PDF-файлу,
    который находится в той же директории, что и метод,
    для считывания содержимого PDF-файла
    :return: абсолютный путь к PDF-файлу в текущей папке
    """
    # Получение текущего пути к файлу
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Формирование полного пути к файлу в текущей папке
    path = os.path.join(current_dir, file_name)
    return path


def extract_text_from_pdf(pdf_path):
    """
    Этот метод получает текст из PDF-файла
    и преобразует его в словарь
    :param pdf_path: путь к PDF-файлу
    :return: считанный текст
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    received_dict = get_dictionary(text)
    pprint(received_dict)
    return received_dict


def compare_content_of_pdf_file():
    """
    Этот метод получает эталонный результат и результат после считывания PDF-файла
    и сравнивает порядок расположения ключей и названия ключей
    :return: True или False
    """
    actual_result = list(extract_text_from_pdf(file_path))
    expected_result = list(data_to_verify)
    print(actual_result)
    print(expected_result)
    compare_dictionaries = all(expected_result[key] == actual_result[key] for key in range(len(expected_result)))
    if compare_dictionaries:
        return "PDF file data conforms to the benchmark"
    else:
        return "PDF file data does not match the benchmark"


file_name = "test_task.pdf"
file_path = get_file_path()
print(compare_content_of_pdf_file())

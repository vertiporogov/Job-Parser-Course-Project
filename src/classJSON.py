import json

from src.classVacancies import Vacancy


class JSONSaver:

    """
    Класс для создания JSON - файла с двнными, и работы с ними.
    """

    def __init__(self):

        self.file = 'vacancy.json'

    def creating_json(self, data):

        """
        Создаёт JSON - файл.
        :param data: информация.
        :return: Файл с декодированной информацией в удобном виде.
        """

        with open(self.file, 'w', encoding='utf-8') as f:

            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancy(self):

        """
        Создание вакансий.
        :return: Список экземпляров класса Vacancy отсортированных по з/п.
        """

        with open(self.file, encoding='utf-8') as f:

            data = json.load(f)

        all_vacancy = []

        for i in data:

            all_vacancy.append(Vacancy(i['name'], i['url'], i['salary_from'], i['salary_to'], i['requirement']))

        sort_ = sorted(all_vacancy, reverse=True)

        return sort_

    def set_salary(self, min_salary, max_salary):

        """
        Сортировка ро з/п.
        :param min_salary: мин.
        :param max_salary: макс.
        :return: Список экземпляров класса Vacancy отсортированных по з/п с указанными параметрами.
        """

        with open(self.file, encoding='utf-8') as f:

            data = json.load(f)

        all_vacancy = []

        for i in data:

            if min_salary <= i['salary_from'] <= max_salary and min_salary <= i['salary_to'] <= max_salary:

                all_vacancy.append(Vacancy(i['name'], i['url'], i['salary_from'], i['salary_to'], i['requirement']))

        sort_ = sorted(all_vacancy, reverse=True)

        return sort_

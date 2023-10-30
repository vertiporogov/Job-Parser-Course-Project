from abc import ABC, abstractmethod

from requests import get

import json


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def format(self, word):
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для получения вакансий с сайта hh.ru"""

    def __init__(self, word):
        self.hh_api = "https://api.hh.ru/vacancies"
        self.word = word

    def get_vacancies(self):

        """Метод для получения списка вакансий"""

        params = {
            'text': f'NAME:{self.word}',
            'area': 2,  # Поиск в зоне
            'page': 0,
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = get(self.hh_api, params=params)
        vacancies = json.loads(response.content.decode())['items']
        return vacancies

    def format(self, word):

        format_list = []
        data = self.get_vacancies()
        for i in data:
            if i['salary']:
                salary_from = i['salary']['from'] if i['salary']['from'] else 0
                salary_to = i['salary']['to'] if i['salary']['to'] else 0
            else:
                salary_from = 0
                salary_to = 0

            format_list.append({
                'name': i['name'],
                'url': i['alternate_url'],
                'salary_from': salary_from,
                'salary_to': salary_to,
                'requirement': i['snippet']['requirement']
            })

        return format_list


class SuperJobAPI(AbstractAPI):

    def __init__(self):
        pass

    def get_vacancies(self, word):
        pass

    def format(self, word):
        pass

# hh = HeadHunterAPI()
# print(hh.get_vacancies('python'))

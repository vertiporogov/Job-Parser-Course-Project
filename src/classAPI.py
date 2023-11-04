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

        for i in word:
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

    def __init__(self, word):

        self.word = word
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self):

        headers = {
            "X-Api-App-Id": 'v3.r..............',
        }
        params = {
            'keyword': {self.word},
            'count': 100,
            'page': 0,
            'period': 0,
            'town': 'Saint-Petersburg',
        }
        response = get(self.url, headers=headers, params=params).json()["objects"]

        return response

    def format(self, word):

        format_list = []

        for i in word:
            format_list.append({
                'name': i['profession'],
                'url': i['link'],
                'salary_from': i['payment_from'],
                'salary_to': i['payment_to'],
                'requirement': i['candidat']
            })

        return format_list

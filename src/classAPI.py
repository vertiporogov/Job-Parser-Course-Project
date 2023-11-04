from abc import ABC, abstractmethod

from requests import get

import json

import os


class AbstractAPI(ABC):

    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self):

        pass

    @abstractmethod
    def format(self, data):

        pass


class HeadHunterAPI(AbstractAPI):
    """
    Класс для получения вакансий с сайта hh.ru.
    """

    def __init__(self, word):

        self.hh_api = "https://api.hh.ru/vacancies"
        self.word = word  # Название профессии которую ищем

    def get_vacancies(self):

        """
        Метод для получения информации с HH.ru.
        :return: Полный список вакансий в JSON - формате.
        """

        params = {
            'text': f'NAME:{self.word}',
            'area': 2,  # Поиск в зоне
            'page': 0,
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = get(self.hh_api, params=params)
        vacancies = json.loads(response.content.decode())['items']

        return vacancies

    def format(self, data):

        """
        :param data: Список словарей в JSON - формате (берём из get_vacancies).
        :return: Cписок словарей в JSON - формате с нужными ключами.
        """

        format_list = []

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

    """
    Класс для получения вакансий с сайта SuperJob.ru.
    """

    api_key: str = os.getenv('API-KEY-SuperJob')  # Получаем токен записанный в переменные окружения

    def __init__(self, word):

        self.word = word  # Название профессии которую ищем
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self):

        """
        Метод для получения информации с SuperJob.ru.
        :return: Полный список вакансий в JSON - формате.
        """

        headers = {
            "X-Api-App-Id": self.api_key,
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

    def format(self, data):

        """
        :param data: Список словарей в JSON - формате (берём из get_vacancies).
        :return: Cписок словарей в JSON - формате с нужными ключами.
        """

        format_list = []

        for i in data:

            format_list.append({
                'name': i['profession'],
                'url': i['link'],
                'salary_from': i['payment_from'],
                'salary_to': i['payment_to'],
                'requirement': i['candidat']
            })

        return format_list

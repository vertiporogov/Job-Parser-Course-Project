from abc import ABC, abstractmethod

from requests import get

import json


class AbstractAPI(ABC):

    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(AbstractAPI):

    """Класс для получения вакансий с сайта hh.ru"""

    def __init__(self):
        self.hh_api = "https://api.hh.ru/vacancies"

    def get_vacancies(self, word):

        """Метод для получения вакансий по слову в названии"""

        params = {
            'text': f'NAME:{word}',
            'area': 2,  # Поиск в зоне
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = get(self.hh_api, params=params)
        vacancies = json.loads(response.content.decode())
        return vacancies['items']


class SuperJobAPI(AbstractAPI):

    def __init__(self):
        pass

    def get_vacancies(self):
        pass


hh = HeadHunterAPI()
print(hh.get_vacancies(['python', 'java']))




from abc import ABC, abstractmethod

from requests import get

import json


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, word):
        pass

    @abstractmethod
    def format(self, word):
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для получения вакансий с сайта hh.ru"""

    def __init__(self):
        self.hh_api = "https://api.hh.ru/vacancies"
        # self.word = word

    def get_vacancies(self, word):

        """Метод для получения списка вакансий"""

        params = {
            'text': f'NAME:{word}',
            'area': 2,  # Поиск в зоне
            'page': 0,
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = get(self.hh_api, params=params)
        vacancies = json.loads(response.content.decode())
        return vacancies['items']

    def format(self, word):

        format_list = []
        data = self.get_vacancies(word)
        for i in data:
            if i['salary'] != None:
                if i['salary']['from'] == None:
                    i['salary']['from'] = 0

                format_list.append({
                    'name': i['name'],
                    'url': i['alternate_url'],
                    'salary_from': i['salary']['from'],
                    'salary_to': i['salary']['to'],
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

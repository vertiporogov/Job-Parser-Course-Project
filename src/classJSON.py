import json

from src.classVacancies import Vacancy


class JSONSaver:

    def __init__(self):

        self.file = 'vacancy.json'

    def creating_json(self, data):

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancy(self):

        with open(self.file, encoding='utf-8') as f:
            data = json.load(f)
        all_vacancy = []
        for i in data:
            all_vacancy.append(Vacancy(i['name'], i['url'], i['salary_from'], i['salary_to'], i['requirement']))

        sort_ = sorted(all_vacancy, reverse=True)

        return sort_

    def set_salary(self, min_salary, max_salary):

        with open(self.file, encoding='utf-8') as f:
            data = json.load(f)
        all_vacancy = []
        for i in data:
            if min_salary <= i['salary_from'] <= max_salary and min_salary <= i['salary_to'] <= max_salary:
                all_vacancy.append(Vacancy(i['name'], i['url'], i['salary_from'], i['salary_to'], i['requirement']))

        sort_ = sorted(all_vacancy, reverse=True)

        return sort_

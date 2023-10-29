class Vacancy:

    def __init__(self, title_vacancy: str, url_vacancy: str, salary_from, salary_to, requirement_vacancy: str):
        self.title_vacancy = title_vacancy
        self.url_vacancy = url_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement_vacancy = requirement_vacancy

    def __str__(self):
        return f'Название: {self.title_vacancy}'

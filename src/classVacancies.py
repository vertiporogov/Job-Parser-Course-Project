class Vacancy:

    """
    Класс для инициализации вакансий и работы с его экземплярами.
    """

    def __init__(self, title_vacancy: str, url_vacancy: str, salary_from, salary_to, requirement_vacancy: str):

        self.title_vacancy = title_vacancy
        self.url_vacancy = url_vacancy
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement_vacancy = requirement_vacancy

    def __repr__(self):

        return f'Vacancy: {self.title_vacancy}'

    def __str__(self):

        return f'Название: {self.title_vacancy}\nТребования: {self.requirement_vacancy}\nЗарплата: от ' \
               f'{self.salary_from} до {self.salary_to}'

    def __lt__(self, other):

        return self.salary_from < other.salary_from

    def __gt__(self, other):

        return self.salary_from > other.salary_from

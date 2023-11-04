from src.classAPI import HeadHunterAPI, SuperJobAPI

from src.classJSON import JSONSaver


def job_parser():

    """
    Программа по парсингу вакансий с одного из двух сайтов (HH.ru или SuperJob.ru) с возможностью выбрать
    минимальное и максимальное значение зарплаты и сортировать от большей к меньшей.
    :return:
    """

    user_title = input('Введите название профессии по которой хотите узнать информацию ')  # Запрос названия профессии от пользователя

    while True:  # ЗАПУСКАЕМ)

        source_selection = int(input('Если хотите получить информацию с сайта HH.ru - введите 1, если с сайта '  # Интересуемся)
                                     'SuperJob.ru - введите 2 '))

        if source_selection == 1:

            hh_api = HeadHunterAPI(user_title)  # Создаём экземпляр класса НН с заданной профессией
            full_list_of_vacancies = hh_api.format(hh_api.get_vacancies())  # Создаём список вакансий в нужном формате
            instance_of_the_json = JSONSaver()  # Создаём экземпляр класса JSONSaver
            instance_of_the_json.creating_json(full_list_of_vacancies)  # Создаем json-файл с данными
            min_salary = int(input('Введите минимальную зарплату - '))
            max_salary = int(input('Введите максимальную зарплату - '))
            result = instance_of_the_json.set_salary(min_salary, max_salary)  # Получаем список вакансий отсартированных от большей з/п к меньшей
            for i in result:  # Выводим в удобном виде
                print(i)
                print('*' * 100)
            break

        elif source_selection == 2:

            sj_api = SuperJobAPI(user_title)  # Создаём экземпляр класса SuperJob с заданной профессией
            full_list_of_vacancies = sj_api.format(sj_api.get_vacancies())  # Создаём список вакансий в нужном формате
            instance_of_the_json = JSONSaver()  # Создаём экземпляр класса JSONSaver
            instance_of_the_json.creating_json(full_list_of_vacancies)  # Создаем json-файл с данными
            min_salary = int(input('Введите минимальную зарплату - '))
            max_salary = int(input('Введите максимальную зарплату - '))
            result = instance_of_the_json.set_salary(min_salary, max_salary)  # Получаем список вакансий отсартированных от большей з/п к меньшей
            for i in result:  # Выводим в удобном виде
                print(i)
                print('*' * 100)
            break

        else:  # Если неправильно выбрали сайт с информацией

            print('Некорректно введен запрос\nДавайте сначала)')
            continue


if __name__ == "__main__":
    job_parser()  # Запускаем программу

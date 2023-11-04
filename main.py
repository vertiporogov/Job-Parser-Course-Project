from src.classAPI import HeadHunterAPI, SuperJobAPI
from src.classJSON import JSONSaver

# hh_api = HeadHunterAPI('администратор')
# f = hh_api.format(hh_api.get_vacancies())

# sj = SuperJobAPI('учитель')
# a = sj.get_vacancies()
# d = sj.format(a)

# print(a)
# print(hh_api.get_vacancies('python')[0])
# f = hh_api.format(hh_api.get_vacancies())
# print(f)
# s = JSONSaver()
# s.creating_json(f)
# g = s.set_salary(30000, 60000)
# g = sorted(g)

# for i in g:
#     print(i)
#     print('*' * 100)
# o = a.set_salary(30000, 60000)
# print(o)
# for i in o:
#     print(i)
#     print('*' * 100)
# print(a)
# for i in hh_api.get_vacancies():
#     if i['salary'] != None:
#         print(i)
# print(hh_api)
# print(*[1, 2, 3])


def job_parser():

    user_title = input('Введите название профессии по которой хотите узнать информацию ')

    while True:

        source_selection = int(input('Если хотите получить информацию с сайта HH.ru введите 1, если с сайта SuperJob.ru введите 2 '))

        if source_selection == 1:

            hh_api = HeadHunterAPI(user_title)
            full_list_of_vacancies = hh_api.format(hh_api.get_vacancies())
            instance_of_the_json = JSONSaver()
            instance_of_the_json.creating_json(full_list_of_vacancies)
            min_salary = int(input('Введите минимальную зарплату '))
            max_salary = int(input('Введите максимальную зарплату '))
            result = instance_of_the_json.set_salary(min_salary, max_salary)
            for i in result:
                print(i)
                print('*' * 100)
            break

        elif source_selection == 2:

            sj_api = SuperJobAPI(user_title)
            full_list_of_vacancies = sj_api.format(sj_api.get_vacancies())
            instance_of_the_json = JSONSaver()
            instance_of_the_json.creating_json(full_list_of_vacancies)
            min_salary = int(input('Введите минимальную зарплату '))
            max_salary = int(input('Введите максимальную зарплату '))
            result = instance_of_the_json.set_salary(min_salary, max_salary)
            for i in result:
                print(i)
                print('*' * 100)
            break

        else:

            print('Некорректно введен запрос\nДавайте сначала)')

            continue


if __name__ == "__main__":
    job_parser()

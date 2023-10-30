from src.classAPI import HeadHunterAPI
from src.classJSON import JSONSaver

hh_api = HeadHunterAPI('администратор')
# print(hh_api.get_vacancies('python')[0])
f = hh_api.format(hh_api.get_vacancies())
# print(f)
a = JSONSaver()
a.creating_json(f)
o = a.set_salary(30000, 60000)
# print(o)
for i in o:
    print(i)
    print('*' * 100)
# print(a)
# for i in hh_api.get_vacancies():
#     if i['salary'] != None:
#         print(i)
# print(hh_api)
# print(*[1, 2, 3])


def job_parser():

    user_title = input('Введите название профессии ')


if __name__ == "__main__":
    pass

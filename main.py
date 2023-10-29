from src.classAPI import HeadHunterAPI
from src.classJSON import JSONSaver

hh_api = HeadHunterAPI()
# print(hh_api.get_vacancies('python')[0])
f = hh_api.format('python')
# print(f)
a = JSONSaver()
a.greating_json(f)
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

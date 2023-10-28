from src.classAPI import HeadHunterAPI

hh_api = HeadHunterAPI()
print(hh_api.get_vacancies()[0])
# for i in hh_api.get_vacancies():
#     if i['salary'] != None:
#         print(i)
# print(hh_api)
# print(*[1, 2, 3])


def job_parser():

    user_title = input('Введите название профессии ')


if __name__ == "__main__":
    pass

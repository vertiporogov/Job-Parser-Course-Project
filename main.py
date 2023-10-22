from src.classAPI import HeadHunterAPI, SuperJobAPI

if __name__ == '__main__':

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")
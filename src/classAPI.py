from abc import ABC, abstractmethod

from requests import get


class AbstractAPI(ABC):

    @abstractmethod
    def get_information(self):
        pass


class HeadHunterAPI(AbstractAPI):

    def __init__(self):
        pass



response = get("https://api.hh.ru/vacancies?employer_id=1740&host=hh.ru")
print(response.__dict__)

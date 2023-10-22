from abc import ABC, abstractmethod

import requests
from requests import get

import json


class AbstractAPI(ABC):

    @abstractmethod
    def get_information(self):
        pass


class HeadHunterAPI(AbstractAPI):

    def __init__(self):
        self.response = get("https://api.hh.ru/vacancies")

    def get_information(self):
        print(self.response.content.decode())



hh = HeadHunterAPI()
hh.get_information()



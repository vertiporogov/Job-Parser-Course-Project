import json

from src.classAPI import HeadHunterAPI


class JSONSaver:

    def __init__(self):
        pass

    def greating_json(self, data):
        with open('vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)


        # return d

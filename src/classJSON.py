import json


class JSONSaver:

    def __init__(self):
        self.file = 'vacancy.json'

    def creating_json(self, data):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # return d

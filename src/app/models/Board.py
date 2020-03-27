import json


class Board(object):
    def __init__(self):
        self.cases = []

        with open('src/ressources/boardData.json') as json_file:
            data = json.load(json_file)
            for case in data['cases']:
                self.cases.append(case)

        # print(self.cases)

# b = Board()
# print(b.cases[39])

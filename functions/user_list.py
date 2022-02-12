import json


class UserList:
    def __init__(self, data):
        data = data.json()
        string = json.dumps(data)
        self.list = json.loads(string)

    def return_list(self):
        return self.list

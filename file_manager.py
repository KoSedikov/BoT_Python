import json

class File:

    def save(self,info):
        with open('file1.txt', 'w') as file1:
            json.dump(info,file1)

    def read(self):
        with open('file1.txt', 'r') as file1:
            return json.load(file1)


    # def __init__(self):
    #     # file1.txt
    #     self.read()

import json


def readJsonData(file):
    with open(file, "r") as f:
        data = json.load(f)
        if not data:
            data = []
        return data


def writeJsonData(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def deleteJsonData(file, array):
    data = readJsonData(file)
    if array in data:
        data.remove(array)
        print(f"Deleted {array} from {file} successfully.")
    writeJsonData(file, data)

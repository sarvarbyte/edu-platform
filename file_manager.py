import csv


def read(path: str)->list:
    with open(path, "r") as file:
        reader = list(csv.reader(file))

    return reader


def write(path: str, data: list) -> None:
    if len(read(path)) == 0:
        with open(path, "w", newline= "") as file:
            writer = csv.writer(file)
            writer.writerow(data)
    else:
        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    print("Data written successfully")

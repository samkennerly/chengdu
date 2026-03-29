"""
Read and write some files.
Use common formats that anyone can read.
"""
import csv
import json

from pathlib import Path

FOLDER = Path(__file__).parent / "files"
HELLO_PATH = FOLDER / "hello.txt"
FRUITS_PATH = FOLDER / "fruits.json"
STUDENTS_PATH = FOLDER / "students.csv"


def read_txt(path):
    print(f"Read text from {path}")
    return path.read_text()


def save_txt(data, path):
    print(f"Save text to {path}")
    path.write_text(data)


def read_json(path):
    print(f"Read JSON data from {path}")
    with open(path) as file:
        return json.load(file)


def save_json(data, path):
    print(f"Save JSON data to {path}")
    with open(path, "w") as file:
        json.dump(data, file, indent=2)


def read_csv(path):
    print(f"Read table from {path}")
    with open(path) as file:
        return list(csv.reader(file, dialect='unix'))


def save_csv(data, path):
    print(f"Save table to {path}")
    with open(path, "w") as file:
        writer = csv.writer(file, dialect='unix')
        for row in data:
            writer.writerow(row)


# Tests


def test_txt(path=HELLO_PATH):
    hello = "Hello, World!"
    print(f"\nTest text: {hello}")

    save_txt(hello, path)
    data = read_txt(path)

    assert data == hello, f"text in {path} is {data}"


def test_json(path=FRUITS_PATH):
    fruits = {
        "apple": "苹果",
        "cherry": "樱桃",
        "pear": "梨子",
        "plum": "李子",
    }
    print(f"\nTest JSON data: {fruits}")

    save_json(fruits, path)
    data = read_json(path)

    assert data == fruits, f"data in {path} is {data}"


def test_csv(path=STUDENTS_PATH):
    students = [
        ["family_name", "given_name", "birthday", "country_code"],
        ["Babbage", "Charles", "1791-12-26", "UK"],
        ["Hopper", "Grace", "1906-12-09", "US"],
        ["Lovelace", "Ada", "1815-12-10", "UK"],
        ["Perlman", "Radia", "1951-12-18", "US"],
        ["Sweigart", "Al", "1985-08-16", "CA"],
        ["Torvalds", "Linus", "1969-12-28", "FI"],
        ["Turing", "Alan", "1912-06-23", "UK"],
        ["van Rossum", "Guido", "1956-01-31", "NL"],
    ]
    print(f"\nTest table:", *students, sep="\n")

    save_csv(students, path)
    data = read_csv(path)

    assert data == students, f"table in {path} is {data}"


test_txt()
test_json()
test_csv()

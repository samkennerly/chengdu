"""
Read and write some files in common text-like formats.
If a program can read plain text, then it can read these files.

This file is also an example of automated testing.
If you run it as a script, it will save some files, then read
those files, and raise an error if anything goes wrong.
"""

import csv
import json

from pathlib import Path

FOLDER = Path(__file__).parent / "data/test"
TXT_PATH = FOLDER / "test.txt"
CSV_PATH = FOLDER / "test.csv"
JSON_PATH = FOLDER / "test.json"


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
        return list(csv.reader(file, dialect="unix"))


def save_csv(data, path):
    print(f"Save table to {path}")
    with open(path, "w") as file:
        writer = csv.writer(file, dialect="unix")
        for row in data:
            writer.writerow(row)


# Tests

def test_txt(path=TXT_PATH):
    hello = "Hello, World!"
    print("\nTest text:")
    print(hello)

    save_txt(hello, path)
    data = read_txt(path)

    assert data == hello, f"text in {path} is {data}"


def test_json(path=JSON_PATH):
    fruits = {
        "apple": ["苹果", "píngguǒ"],
        "cherry": ["樱桃", "yīngtáo"],
        "pear": ["梨子", "lízǐ"],
        "plum": ["李子", "lǐzǐ"],
    }
    print("\nTest JSON data:")
    for key, value in fruits.items():
        print(f"{key}: {value}")

    save_json(fruits, path)
    data = read_json(path)

    assert data == fruits, f"data in {path} is {data}"


def test_csv(path=CSV_PATH):
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
    print("\nTest table:")
    for row in students:
        print(row)

    save_csv(students, path)
    data = read_csv(path)

    assert data == students, f"table in {path} is {data}"


test_txt()
test_json()
test_csv()

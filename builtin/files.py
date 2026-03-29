"""
Read and write some files.
Use common formats that anyone can read.
"""

from pathlib import Path

FOLDER = Path(__file__).resolve().parent / "files"
HELLO_PATH = HERE / "hello.txt"
FRUITS_PATH = HERE / "fruits.json"
STUDENTS_PATH = HERE / "students.csv"


def read_txt(path):
    print(f"Read text from {path}")
    raise NotImplementedError


def save_txt(data, path):
    print(f"Save text to {path}")
    raise NotImplementedError


def read_json(path):
    print(f"Read JSON data from {path}")
    raise NotImplementedError


def save_json(data, path):
    print(f"Save JSON data to {path}")
    raise NotImplementedError


def read_csv(path):
    print(f"Read table from {path}")
    raise NotImplementedError


def save_csv(data, path):
    print(f"Save table to {path}")
    raise NotImplementedError


# Tests


def test_txt(path=HELLO_PATH):
    hello = "Hello, World!\n"
    save_text(hello, path)

    data = read_txt(path)

    assert data == hello, f"text in {path} does not match original"


def test_json(path=FRUITS_PATH):
    fruits = {
        "apple": "苹果",
        "cherry": "樱桃",
        "pear": "梨子",
        "plum": "李子",
    }
    save_json(fruits, path)

    data = read_json(path)

    assert data == fruits, f"data in {path} does not match original"


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
    save_json(students, path)

    data = read_csv(path)

    assert data == students, f"table in {path} does not match original"


test_txt()
test_json()
test_csv()

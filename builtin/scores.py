"""
Example function from Prof. Li Bo's class 2026-03-26.
"""

def get_average_score(file_name):
    """
    Read a space-separated value file.
    Assume the last column is student scores.
    Return the average of all scores.
    """

    print(f"Get scores from {file_name}")
    with open(file_name) as f:
        lines = f.readlines()

    zongfen = 0
    for line in lines:
        fenshu = line.strip().split(' ')[-1]
        zongfen += float(fenshu)

    return zongfen / len(lines)


folder = "data/scores"
files = [f"{folder}/hw{x}.txt" for x in (1,2,3)]

print(f"Average score is {avg_score}")

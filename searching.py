import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)

    return data[field]


def linear_search(unordered_numbers, searched_number):
    index = []
    count_number = 0
    for idx, number in enumerate(unordered_numbers):
        if searched_number == number:
            index.append(idx)
            count_number += 1
    dict = {"positions": index, "count": count_number}
    return dict


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    searched_number = 0
    search = linear_search(unordered_numbers, searched_number)
    print(search)


if __name__ == '__main__':
    main()
import re


def get_lines(content):
    all_lines = [line.strip() for line in content.readlines()]
    return all_lines


def file_check(lines):
    """
    :param lines: list
    :return: string
    """
    if not lines[0].isdigit():
        raise ValueError("first line should be an integer (number of curry types)")
    for i in range(1, len(lines)):
        if not lines[i]:
            raise ValueError("file not valid, please remove all empty lines")
        num, let = extract_num_let(lines[i])
        if not num or not let:
            raise ValueError(f"error with client {i}, no preference found")
        if len(num) != len(let):
            raise ValueError(f"error with client {i}, each curry type need a preference between M and V")
        if "M" not in lines[i] and "V" not in lines[i]:
            raise ValueError(f"error with client {i}, at least one preference between Meat and Veggie should be present")
    return "ok"


def extract_num_let(pref, n_curries=""):
    """
    :param pref: list with preferences
    :param n_curries: integer (number of available curries)
    :return: tuple with two lists
    """
    numbers, letters = re.findall(r'\d+', pref), re.findall(r'[a-zA-z]+', pref)
    try:
        check_availability(numbers, n_curries)
    except ValueError:  # raised when n_curries is not provided
        pass
    return numbers, letters


def check_availability(preferred_curries, n_curries):
    """
    :param preferred_curries: list
    :param n_curries: string
    :return: None
    """
    for n in preferred_curries:
        if int(n) > int(n_curries) or int(n) < 1:
            raise TypeError(f"error: curry type {n} is not available")

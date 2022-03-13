#!/usr/bin/env python3
"""project:Election Data, created:1/26/2022, author:seraph★776"""


def get_file(filename) -> list:
    """Open election_data from file"""
    with open(filename) as fo:
        content = [i.strip() for i in fo.readlines()]
    return content


def process_file(data: list) -> list:
    """Changes the string-digits into integers"""
    election_data = [i.split(' ') for i in data]
    # Change string-digits to integers:
    for i, candidate in enumerate(election_data):
        for j, field in enumerate(candidate):
            if field.isdigit():
                election_data[i][j] = int(election_data[i][j])
    return election_data


def separate_by_district(data) -> dict:
    """Separate election_data by district and sort each list by vote in descending order"""
    # Sort each district by total winning votes in descending order
    d1 = sorted([i for i in data if i[2] == 1], key=lambda i: i[3], reverse=True)
    d2 = sorted([i for i in data if i[2] == 2], key=lambda i: i[3], reverse=True)
    d3 = sorted([i for i in data if i[2] == 3], key=lambda i: i[3], reverse=True)
    d4 = sorted([i for i in data if i[2] == 4], key=lambda i: i[3], reverse=True)
    d5 = sorted([i for i in data if i[2] == 5], key=lambda i: i[3], reverse=True)
    d6 = sorted([i for i in data if i[2] == 6], key=lambda i: i[3], reverse=True)
    d7 = sorted([i for i in data if i[2] == 7], key=lambda i: i[3], reverse=True)
    d8 = sorted([i for i in data if i[2] == 8], key=lambda i: i[3], reverse=True)
    d9 = sorted([i for i in data if i[2] == 9], key=lambda i: i[3], reverse=True)
    d10 = sorted([i for i in data if i[2] == 10], key=lambda i: i[3], reverse=True)
    # Store districts in a dictionary for easier retrieval:
    districts = {k: v for (k, v) in enumerate([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10], start=1)}
    return districts


def omega_red(s) -> str:
    """Changes string color output to red"""
    s = '\033[1;91m' + s + '\033[0m'
    return s


def display_results(data) -> None:
    """Displays the results of election_data"""
    print(' --- Winners by District ---  '.center(50))
    for key, district in data.items():
        # Get total votes for entire district:
        total_votes = sum([i[3] for i in district])
        for i, item in enumerate(district):
            first_name, last_name = item[0], item[1]
            winning_votes = item[3]
            if i == 0:  # Because Index zero is the winner:
                print(f"DISTRICT #{key}: {' '.join([first_name, last_name])} "
                      # The color graph
                      f"{omega_red('|' * int(winning_votes / total_votes * 100 / 2))} "
                      f"{winning_votes / total_votes * 100:.2f}% ")


def main():
    election_data = get_file('election.dat')
    election_data = process_file(election_data)
    election_data = separate_by_district(election_data)
    display_results(election_data)


if __name__ == '__main__':
    main()

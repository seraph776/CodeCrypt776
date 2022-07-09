def print_pattern(word):
    for row in range(0, len(word)):
        st = ""
        for col in range(0, row):
            st += " "
        st += word[row]
        print(st)


if __name__ == '__main__':
    print_pattern('codewars')

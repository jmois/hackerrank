def count_substring(string, sub_string):
    i = 0
    count = 0
    total = len(string)
    while (i != -1):
        i = string.find(sub_string)
        if (i != -1):
            count += 1
            string = string[i + 1:]

    return count


if __name__ == '__main__':
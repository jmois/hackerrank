def mutate_string(string, position, character):
    string = string[:int(position)] + str(character) + string[int(position)+1:]
    return string

if __name__ == '__main__':
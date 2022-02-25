import random

lower_limit = 0
upper_limit = 1000


def to_memory(input_size):
    input_list = []
    for i in range(int(input_size)):
        n = random.randint(lower_limit, upper_limit)
        input_list.append(n)
    return input_list


def to_file(input_size, file_name):
    with open(file_name, 'w') as file_writer:
        for i in range(int(input_size)):
            file_writer.write(str(random.randint(lower_limit, upper_limit)) + "\n")
        file_writer.close()

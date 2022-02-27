import random


def to_memory(input_size, input_range):
    input_list = []
    for i in range(int(input_size)):
        n = random.randint(input_range[0], input_range[1])
        input_list.append(n)
    return input_list


def to_file(input_size, input_range, file_name):
    with open(file_name, 'w') as file_writer:
        for i in range(int(input_size)):
            file_writer.write(str(random.randint(input_range[0], input_range[1])) + "\n")
        file_writer.close()


def to_file(input_list, file_name):
    with open(file_name, 'w') as file_writer:
        for i in input_list:
            file_writer.write(str(i) + "\n")
        file_writer.close()

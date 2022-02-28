import random


def to_memory(input_size, input_range):
    input_list = []
    for i in range(int(input_size)):
        n = random.randint(input_range[0], input_range[1])
        input_list.append(n)
    return input_list


def to_file(input_size, input_range, file_name):
    print("Generating input to file: " + file_name)
    with open(file_name, 'w') as file_writer:
        for i in range(int(input_size)):
            file_writer.write(str(random.randint(input_range[0], input_range[1])) + "\n")
        file_writer.close()
    return input_size


def list_to_file(input_list, file_name):
    print("Writing output to file: " + file_name)
    with open(file_name, 'w') as file_writer:
        for i in input_list:
            file_writer.write(str(i) + "\n")
        file_writer.close()


def from_file(file_name):
    print("Reading input from file: " + file_name)
    input_list = []
    with open(file_name, 'rb') as file_reader:
        for number in file_reader:
            if not number:
                break
            input_list.append(int(number))
    file_reader.close()
    return input_list

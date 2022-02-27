import generate_input


class MergeSort:
    def sort(self, list):
        list_length = len(list)

        if list_length == 1:
            return list

        mid_point = list_length // 2

        left_partition = self.sort(list[:mid_point])
        right_partition = self.sort(list[mid_point:])

        return self.merge(left_partition, right_partition)

    def merge(self, left, right):
        output = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])

        return output


def generate_and_sort(input_size, input_range):
    input = generate_input.to_memory(input_size, input_range)
    ms = MergeSort()
    ms.sort(input)


def list_sort(input_list):
    ms = MergeSort()
    ms.sort(input_list)


if __name__ == "__main__":
    generate_and_sort(100, (0, 10000))

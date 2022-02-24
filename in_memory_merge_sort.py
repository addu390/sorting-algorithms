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


def with_random_numbers(input_size):
    input = generate_input.to_memory(input_size)
    ms = MergeSort()
    ms.sort(input)


if __name__ == "__main__":
    with_random_numbers(100)

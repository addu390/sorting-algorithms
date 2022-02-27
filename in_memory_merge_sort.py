import file_util


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


def _random(input_size, input_range):
    input = file_util.to_memory(input_size, input_range)
    ms = MergeSort()
    ms.sort(input)


def sort_from_file(file_name, input_size):
    input = file_util.from_file(file_name)
    print(len(input))
    ms = MergeSort()
    ms.sort(input)


if __name__ == "__main__":
    _random(100, (0, 10000))

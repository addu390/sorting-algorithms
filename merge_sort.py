import generate_input


class MergeSort:
    def mergeSort(self, input_list):
        if len(input_list) > 1:
            mid = len(input_list) // 2
            left = input_list[:mid]
            right = input_list[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    input_list[k] = left[i]
                    i += 1
                else:
                    input_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                input_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                input_list[k] = right[j]
                j += 1
                k += 1


def default(input_size):
    print("Merge Sort: " + str(input_size))
    input = generate_input.to_memory(input_size)
    ms = MergeSort()
    ms.mergeSort(input)


if __name__ == "__main__":
    default(10)

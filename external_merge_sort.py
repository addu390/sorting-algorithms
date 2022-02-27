import os
import sys
import tempfile
import glob
import generate_input


class HeapNode:
    def __init__(self, element, chuck_file):
        self.element = element
        self.chunk_file = chuck_file


class ExternalMergeSort:
    def __init__(self):
        self.chunk_files = []

    def run(self, input_file_name, output_file_name, chunk_size=10000):
        if os.path.exists('./temp'):
            self.clear()
        else:
            os.mkdir('./temp')

        self.split(input_file_name, chunk_size)
        self.merge_chunks(output_file_name)
        self.clear()

    def construct_heap(self, arr):
        length = len(arr)
        mid = length // 2
        while mid >= 0:
            self.heapify(arr, mid, length)
            mid -= 1

    def heapify(self, heap, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and heap[left].element < heap[i].element:
            min_element = left
        else:
            min_element = i

        if right < n and heap[right].element < heap[min_element].element:
            min_element = right

        if i != min_element:
            (heap[i], heap[min_element]) = (heap[min_element], heap[i])
            self.heapify(heap, min_element, n)

    def merge_chunks(self, output_file_name):
        heap = []
        with open(output_file_name, 'w') as file_writer:
            for chunk_file in self.chunk_files:
                element = int(chunk_file.readline().strip())
                heap.append(HeapNode(element, chunk_file))

            self.construct_heap(heap)

            while True:
                top = heap[0]
                if top.element == sys.maxsize:
                    break
                file_writer.write(str(top.element) + "\n")
                file_reader = top.chunk_file
                element = file_reader.readline().strip()
                if not element:
                    element = sys.maxsize
                else:
                    element = int(element)
                heap[0] = HeapNode(element, file_reader)
                self.heapify(heap, 0, len(heap))
        file_writer.close()

    def split(self, file_name, chunk_size):
        with open(file_name, 'rb') as file_reader:
            size = 0
            sorted_chunk = []

            for number in file_reader:
                if not number:
                    break
                sorted_chunk.append(number)
                size += 1
                if size % chunk_size == 0 and len(sorted_chunk) != 0:
                    sorted_chunk = sorted(sorted_chunk, key=lambda no: int(no.strip()))
                    self.save_chunk(sorted_chunk)
                    sorted_chunk = []
            if len(sorted_chunk) > 0:
                self.save_chunk(sorted_chunk)

    def save_chunk(self, sorted_chunk):
        temp_file = tempfile.NamedTemporaryFile(dir=os.getcwd() + '/temp', delete=False)
        temp_file.writelines(sorted_chunk)
        temp_file.seek(0)
        self.chunk_files.append(temp_file)

    def clear(self):
        files = glob.glob(os.getcwd() + '/temp/*')
        for f in files:
            os.remove(f)


def generate_and_sort(input_size, chunk_size, input_range):
    input_file_name = "unsorted.csv"
    output_file_name = "sorted.csv"

    generate_input.to_file(input_size, input_range, input_file_name)
    ems = ExternalMergeSort()
    ems.run(input_file_name, output_file_name, chunk_size if input_size > chunk_size else input_size)


def list_sort(input_list, chunk_size):
    input_file_name = "unsorted.csv"
    output_file_name = "sorted.csv"

    generate_input.to_file(input_list, input_file_name)
    ems = ExternalMergeSort()
    ems.run(input_file_name, output_file_name, chunk_size if len(input_list) > chunk_size else len(input_list))


if __name__ == "__main__":
    generate_and_sort(100, 10, (0, 10000))


import math
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

    def merge_chunks(self):
        heap = []
        sorted_output = []
        for chunk_file in self.chunk_files:
            element = int(chunk_file.readline().strip())
            heap.append(HeapNode(element, chunk_file))

        self.construct_heap(heap)

        while True:
            top = heap[0]
            if top.element == sys.maxsize:
                break
            sorted_output.append(top.element)
            file_reader = top.chunk_file
            element = file_reader.readline().strip()
            if not element:
                element = sys.maxsize
            else:
                element = int(element)
            heap[0] = HeapNode(element, file_reader)
            self.heapify(heap, 0, len(heap))
        return sorted_output

    def split(self, file_name, chunk_size):
        with open(file_name, 'rb') as file_reader:
            size = 0
            sorted_chunk = []

            for number in file_reader:
                if not number:
                    break
                sorted_chunk.append(number)
                size += 1
                if size % chunk_size == 0:
                    sorted_chunk = sorted(sorted_chunk, key=lambda no: int(no.strip()))
                    temp_file = tempfile.NamedTemporaryFile(dir=os.getcwd() + '/temp', delete=False)
                    temp_file.writelines(sorted_chunk)
                    temp_file.seek(0)
                    self.chunk_files.append(temp_file)
                    sorted_chunk.clear()

    def clear(self):
        files = glob.glob(os.getcwd() + '/temp/*')
        for f in files:
            os.remove(f)


def default(input_size):
    print("External Sort: " + str(input_size))
    generate_input.to_file(input_size)
    ems = ExternalMergeSort()
    ems.split(generate_input.file_name, math.ceil(input_size/1000))
    ems.clear()


if __name__ == "__main__":
    default(100)


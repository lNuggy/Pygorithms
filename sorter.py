from colorama import Fore
import random
import json
import argparse
import time


class Algorithms:
    def bubble_sort(arr):
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def counting_sort(arr):
        max_value = max(arr) + 1
        count = [0] * max_value
        for i in arr:
            count[i] += 1
        j = 0
        for i in range(max_value):
            for k in range(count[i]):
                arr[j] = i
                j += 1
        return arr

    def shell_sort(arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def selection_sort(arr):
        n = len(arr)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def gnome_sort(arr):
        n = len(arr)
        i = 0
        while i < n:
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr

    def shell_sort(arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def selection_sort(arr):
        n = len(arr)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def gnome_sort(arr):
        n = len(arr)
        i = 0
        while i < n:
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        return arr

    def shell_sort(arr):
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr

    def cocktail_sort(arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            start = start + 1
        return arr

    def comb_sort(arr):
        n = len(arr)
        gap = n
        shrink = 1.3
        swapped = True
        while gap > 1 or swapped:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1
            swapped = False
            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
        return arr

    def pigeonhole_sort(arr):
        min_val = min(arr)
        max_val = max(arr)
        size = max_val - min_val + 1
        holes = [0] * size
        for x in arr:
            holes[x - min_val] += 1
        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                arr[i] = count + min_val
                i += 1
        return arr

    def stooge_sort(arr):
        n = len(arr)
        if n <= 2:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            return arr
        m = int(n / 3)
        arr[: n - m] = Algorithms.stooge_sort(arr[: n - m])
        arr[m:] = Algorithms.stooge_sort(arr[m:])
        arr[: n - m] = Algorithms.stooge_sort(arr[: n - m])
        return arr

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Algorithms.merge_sort(L)
            Algorithms.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return Algorithms.quick_sort(left) + middle + Algorithms.quick_sort(right)

    def cocktail_sort(arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            start = start + 1
        return arr

    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort numbers in a JSON file")
    parser.add_argument("file", metavar="file", type=str, help="path to JSON file")
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=[
            "stooge",
            "pigeonhole",
            "gnome",
            "bubble",
            "selection",
            "insertion",
            "shell",
            "cocktail",
            "heap",
            "merge",
            "quick",
            "comb",
            "counting",
        ],
        default="bubble",
        help="sorting algorithm",
    )
    parser.add_argument(
        "-g",
        "--generate",
        metavar="n",
        type=int,
        help="generate a JSON file containing n numbers",
    )
    parser.add_argument(
        "--min",
        "-mn",
        type=int,
        default=0,
        help="minimum value for generated numbers",
    )
    parser.add_argument(
        "--max",
        "-mx",
        type=int,
        default=1000,
        help="maximum value for generated numbers",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="print the sorted array",
    )

    args = parser.parse_args()

    if args.generate:

        data = [random.randint(args.min, args.max) for _ in range(args.generate)]
        with open(args.file, "w") as f:
            json.dump(data, f)
        print(f"Generated JSON file containing {args.generate} numbers at {args.file}")
        exit()

    try:
        with open(args.file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(Fore.RED + "File not found or does not exist!" + Fore.RESET)
        exit()

    arr = data

    start_time = time.time()

    sorted_arr = eval(f"Algorithms.{args.algorithm}_sort(arr)")

    end_time = time.time()

    if args.debug:

        print(sorted_arr)

    execution_time = end_time - start_time

    if execution_time < 0.01:
        print(Fore.GREEN + "Execution time: {} seconds".format(execution_time))
    elif execution_time < 0.2:
        print(Fore.LIGHTGREEN_EX + "Execution time: {} seconds".format(execution_time))
    elif execution_time < 1.0:
        print(Fore.GREEN + "Execution time: {} seconds".format(execution_time))
    elif execution_time < 2.0:
        print(Fore.YELLOW + "Execution time: {} seconds".format(execution_time))
    elif execution_time < 4.0:
        print(Fore.LIGHTYELLOW_EX + "Execution time: {} seconds".format(execution_time))
    else:
        print(Fore.RED + "Execution time: {} seconds".format(execution_time))

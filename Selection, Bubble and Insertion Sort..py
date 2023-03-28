def selection_sort(data):
    for i in range(len(data)):
        minimum = data[i]
        for j in range(i, len(data)):
            if data[j] <= minimum:
                minimum = data[j]
                position = j
        temp_data = data[i]
        data[i] = minimum
        data[position] = temp_data
    return data


def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp_data = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp_data
    return data


def insertion_sort(data):
    for i in range(len(data)):
        for j in reversed(range(i)):
            if data[j] > data[j + 1]:
                temp_data = data[j + 1]
                data[j + 1] = data[j]
                data[j] = temp_data
    return data

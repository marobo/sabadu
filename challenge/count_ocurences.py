my_list = [1, 2, 1, 3, 3, 2, 4, 5, 3, 'a', 'a', 'b', 'c', 'c']


def count_ocurence(my_list):
    occurences = {}
    keys = set(my_list)
    for key in keys:
        number_of_time_found = 0
        for item in my_list:
            if item == key:
                number_of_time_found += 1
        occurences[key] = number_of_time_found
    return occurences

count_ocurence(my_list)

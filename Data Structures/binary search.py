pos = -1


def binary_search(list_given, searched_element):
    lower_bound = 0
    upper_bound = len(list_given) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if list_given[mid] == searched_element:
            globals()['pos '] = mid
            return True
        else:
            if list_given[mid] < searched_element:
                lower_bound = mid+1
            else:
                upper_bound = mid+1

        return False


list1 = [4, 7, 8, 12, 45, 99, 102, 702, 10997, 56666]
n = 10987

if binary_search(list1, n):
    print("Found", pos + 1)
else:
    print("Not Found")

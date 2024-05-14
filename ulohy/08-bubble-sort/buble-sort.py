
# without optimization O(n) = (n-1)**2
def bubble_sort_1(items:list)->list:
    for j in range(len(items)-1):
        for i in range(0, len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items

# easy optimalization O(n) = ((n-1)**2)/2
def bubble_sort_2(items:list)->list:
    for j in range(len(items)-1):
        for i in range(0, len(items) - j - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items


# better optimalization O(n) <= ((n-1)**2)/2
def bubble_sort_3(items:list)->list:
    for j in range(len(items)-1):
        swaps = 0
        for i in range(0, len(items) - j - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swaps += 1
        if swaps == 0:
            break
    return items


print(bubble_sort_3([5, 8, 1, 4, 2, 6]))

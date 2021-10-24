#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(N) Iterate through the list only once
    Memory usage: O(1) No more container was created """
    return all(items[i] <= items[i+1] for i in range(len(items)-1))


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(N^2) 
    Memory usage: O(1) No more container was created """
    isSorted = False
    last_index = len(items) - 1
    # Repeat until all items are in sorted order
    while not isSorted:

        isSorted = True
        for i in range(last_index):
            # Swap adjacent items that are out of order
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                isSorted = False
        last_index -= 1
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(N^2) 
    Memory usage: O(1)"""

    start_index = 0
    while start_index < len(items):
        # Repeat until all items are in sorted order
        min_index = start_index
        for i in range(start_index, len(items)):
            # Find minimum item in unsorted items
            if items[i] < items[min_index]:
                min_index = i
        # Swap it with first unsorted item
        items[start_index], items[min_index] = items[min_index], items[start_index]
        start_index += 1
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(N^2)
    Memory usage: O(1) """

    # Repeat until all items are in sorted order
    for i in range(1, len(items)):
        cur_val = items[i]
        j = i-1
        while j >= 0 and cur_val < items[j]:
            # Take first unsorted item
            items[j+1] = items[j]
            j -= 1
        # Insert it in sorted order in front of items
        items[j+1] = cur_val

    return items

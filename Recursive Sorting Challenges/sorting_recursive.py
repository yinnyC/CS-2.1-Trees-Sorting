#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    # Running time: ??? Why and under what conditions?
    # Memory usage: ??? Why and under what conditions?"""
    if items1 == []:
        return items2
    if items2 == []:
        return items1
    if items1 != [] and items2 != []:
        if items1[0] < items2[0]:
            return [items1[0]] + merge(items1[1:], items2)
        else:
            return [items2[0]] + merge(items1, items2[1:])


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) <= 1:
        return items
    mid_point = len(items) // 2
    left = merge_sort(items[:mid_point])
    right = merge_sort(items[mid_point:])
    return merge(left, right)


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    # Best case running time: O(n log n) when the list is already sorted
    # Worst case running time: O(n^2)
    # Memory usage: O(1) In-Place algo"""
    length = len(items)
    if length <= 1:
        return items
    else:
        pivot = items.pop()
    left = []
    right = []
    for item in items:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([10, 5, 2, 3]))

#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k)
    Memory usage: O(n+k)
    """
    # Find range of given numbers (minimum and maximum integer values)
    min_num = min(numbers)
    max_num = max(numbers)
    num_range = max_num - min_num + 1
    # Create list of counts with a slot for each number in input range
    count_arr = [0] * num_range
    # Loop over given numbers and increment each number's count
    for num in numbers:
        count_arr[num - min_num] += 1
    # Loop over counts and append that many numbers into output list]
    output = []
    for num in range(num_range):
        output += [num + min_num] * count_arr[num]
    return output


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k)
    Memory usage: O(n+k)
    """
    # Find range of given numbers (minimum and maximum values)
    min_num = min(numbers)
    max_num = max(numbers)
    num_range = max_num - min_num + 1
    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]
    # Loop over given numbers and place each item in appropriate bucket
    for num in numbers:
        buckets[(num - min_num) // (num_range // num_buckets)].append(num)
    # Sort each bucket using any sorting algorithm (recursive or another)
    for bucket in buckets:
        bucket.sort()
    # Concatenate all buckets into a single sorted list
    output = []
    for bucket in buckets:
        output += bucket
    return output


print(bucket_sort([2, 1, 4, 7, 10, 3, 5, 6, 9, 8]))

# ============================================================
# SEARCH ALGORITHM ANALYSIS
# ============================================================


def linear_search(arr, target):
    """
    Search for target using Linear Search.

    Returns:
        index: First index where target is found, otherwise -1
        comparisons: Number of elements checked
    """

    comparisons = 0

    for i, value in enumerate(arr):

        comparisons += 1

        if value == target:
            return i, comparisons

    return -1, comparisons


def binary_search(arr, target):
    """
    Search for target using Binary Search.

    The array must be sorted.

    Returns:
        index: First index where target is found, otherwise -1
        comparisons: Number of elements checked
    """

    low = 0
    high = len(arr) - 1

    result = -1
    comparisons = 0

    while low <= high:

        mid = (low + high) // 2

        comparisons += 1

        if arr[mid] == target:

            result = mid

            # Continue searching on the left
            # to find the first occurrence.
            high = mid - 1

        elif arr[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return result, comparisons

if __name__ == "__main__":

    data = [10, 20, 20, 20, 30, 40, 50]

    target = 20

    linear_result = linear_search(data, target)
    binary_result = binary_search(data, target)

    print("Linear Search:")
    print("Index:", linear_result[0])
    print("Comparisons:", linear_result[1])

    print()

    print("Binary Search:")
    print("Index:", binary_result[0])
    print("Comparisons:", binary_result[1])
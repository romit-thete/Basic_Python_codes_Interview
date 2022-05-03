"""
Bubble sort is a sorting algorithm that compares two adjacent elements and
swaps them until they are not in the intended order.

Just like the movement of air bubbles in the water that rise up to the surface,
each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.

"""


def bubbleSort(list_of_elems):
    # Get the total number of elements
    total_elems = len(list_of_elems)

    # Start a loop for the total number of terms (index starts at 0)
    for i in range(total_elems - 1):
        # Start a loop that'll span from 1st element up to the last element followed by second last element and so on.
        for j in range(total_elems - i - 1):
            # Compare the current and the next element
            if list_of_elems[j] > list_of_elems[j + 1]:
                # Swap positions if the first element is greater than the second.
                list_of_elems[j], list_of_elems[j + 1] = list_of_elems[j + 1], list_of_elems[j]
    return list_of_elems


elem_list = [22, 11, 34, 5, 6, 77, 44, 12, 47]
print(bubbleSort(elem_list))

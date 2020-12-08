# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    if len(sequence) == 1:
        return list(sequence)
    else:
        up_ls = []
        pre_ls = get_permutations(sequence[1:])

        for element in pre_ls:
            for i in range(len(element) + 1):
                tmp = list(element[:])
                tmp.insert(i, sequence[0])
                up_ls.append("".join(tmp))

    return sorted(up_ls)


if __name__ == "__main__":
    #    #EXAMPLE
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations(example_input))
    print()
    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
    example_input = "!.?"
    print("Input:", example_input)
    print("Expected Output:", ["!.?", "!?.", ".!?", ".?!", "?!.", "?.!"])
    print("Actual Output:", get_permutations(example_input))
    print()

    example_input = "xy"
    print("Input:", example_input)
    print("Expected Output:", ["xy", "yx"])
    print("Actual Output:", get_permutations(example_input))

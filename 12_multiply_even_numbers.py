def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    import functools
    even_numbers = [num for num in nums if num % 2 == 0]

    if even_numbers :
        return functools.reduce(lambda a, b : a * b, even_numbers)
        #reduce(lambda accum, curr: accum * curr, list)
    else :
        return 1





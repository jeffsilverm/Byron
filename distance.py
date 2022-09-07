#! /usr/bin/python3
#
# This code some discussions about distance functions, sent to me
# (Jeff Silverman, JHS) from Byron Silverman September 5th, 2022
# It is a discussion of common distance metrics between integers


def distance_byron_1(a, b):
    """ This function calculates a distrance metric between two integers.  a,b
    This is the original version
    """
    if a - b >= 0:
        return a - b
    else:
        #        return a-b+(2(a-b))  int objects are not collable
        return a - b + (2 * (
                a - b))  # This is a computer program, not an algebra
        # treatise


def distance_byron_2(a, b):
    """ This function calculates a distrance metric between two integers.  a,b
    But it uses a loop.
    This is the original version
    """
    # If a == b, then a-b = 0.  0 % 2 is 0.  Raised to any power is 1.
    assert a != b, f" {a} == {b} and that will cause an infinite loop"
    # j is referenced before definition.  So I (JHS) am taking a guess at
    # you (BS) meant
    j = 0
    r = None  # PyCharm detected a possible reference before assign error.
    # By analysis, this could happen if ((a - b) % 2 ** j != 0
    # on the first iteration
    while (a - b) % 2 ** j == 0:
        r = 1 / 2 ** j
        j = j + 1
    return r


def distance_jeff_1(a: int, b: int) -> int:
    """ This function calculates a distance metric between two integers.  a,b
    This is Jeff's version, with some changes for good coding practices
    """
    assert isinstance(a, int), f"a is a {type(a)}, should be an int"
    assert isinstance(b, int), f"b is a {type(b)}, should be an int"
    # In your letter of 2022-09-05, you mentioned a constraint of a >= b
    # If that constraint is really important, then the following test will
    # be false
    if a - b >= 0:
        return a - b
    else:
        # a - b + (2*(a-b))
        # a - b + 2*a - 2*b
        # 3*a - 3*b
        # 3*( a - b )
        return 3 * (a - b)


def distance_jeff_2(a: int, b: int) -> float:
    """ This function calculates a distance metric between two integers.  a,b
    But it uses a loop.
    This is Jeff's modified version
    """
    # If a == b, then a-b = 0.  0 % 2 is 0.  Raised to any power is 1.
    assert isinstance(a, int), f"a is a {type(a)}, should be an int"
    assert isinstance(b, int), f"b is a {type(b)}, should be an int"
    assert a != b, f" {a} == {b} and that will cause an infinite loop"

    # j is referenced before definition.  So I (JHS) am taking a guess at
    # you (BS) meant
    j = 0
    r = None
    while (a - b) % 2 ** j == 0:
        r = 1 / 2 ** j
        j = j + 1
    return r


def test_function(test_case_name, function_under_test):
    """ This function tests constance distance metric
     functions both for "reasonable" cases and "patholical" cases."""

    print("*" * 10, test_case_name, "+" * 10)
    a = 4
    b = 3
    r = function_under_test(a, b)
    print("small distance: ", a, b, r)
    a, b = 100_000, 3
    r = function_under_test(a, b)
    print("large distance: ", a, b, r)
    try:
        a, b = 3, 3
        r = function_under_test(a, b)
        print("zero distance: ", a, b, r)
    except AssertionError:
        print("The zero distance case raised an Assertion error")
    a, b = 3, 4
    r = function_under_test(a, b)
    print("Small negative distance: ", a, b, r)
    a, b = 3, 100_000
    r = function_under_test(a, b)
    print("large negative distance: ", a, b, r)


def test_function_jeffs_way(test_case_name, function_under_test):
    """ This function tests constance distance metric
     functions both for "reasonable" cases and "patholical" cases."""

    print("*" * 10, test_case_name, "+" * 10)
    a = 4
    b = 3
    r: int = function_under_test(a, b)
    print("small distance: ", a, b, r)
    a, b = 100_000, 3
    r: int = function_under_test(a, b)
    print("large distance: ", a, b, r)
    try:
        a, b = 3, 3
        r: int = function_under_test(a, b)
        print("zero distance: ", a, b, r)
    except AssertionError:
        print("The zero distance case raised an Assertion error")
    a, b = 3, 4
    r: int = function_under_test(a, b)
    print("Small negative distance: ", a, b, r)
    a, b = 3, 100_000
    r: int = function_under_test(a, b)
    print("large negative distance: ", a, b, r)

    a = 4.0
    b = 3
    try:
        r: int = function_under_test(a, b)
        print("pathological case: floating small distance: ", a, b, r)
    except AssertionError:
        print(
            f"arguments {a}, {b} to {function_under_test.__name__} raised an "
            f"AssertionError exception ")


def main():
    test_function(test_case_name="Byron's first distance function",
                  function_under_test=distance_byron_1)
    test_function(test_case_name="Byron's second distance function",
                  function_under_test=distance_byron_2)
    test_function(test_case_name="Jeff's first distance function",
                  function_under_test=distance_jeff_1)
    test_function_jeffs_way(test_case_name="Jeff's first distance function",
                            function_under_test=distance_jeff_1)


if "__main__" == __name__:
    main()

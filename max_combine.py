from functools import cmp_to_key
from typing import List


def max_combine(xs: List[int]) -> int:
    if not xs:
        return 0
    nums = [x for x in xs if isinstance(x, int) and x >= 0]
    if not nums:
        return 0

    def comparator(a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    joined = ''.join(sorted(map(str, nums), key=cmp_to_key(comparator)))
    return 0 if joined[0] == '0' else int(joined)


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 3, 4, 55], 554331),
        ([71, 45, 23, 4, 5], 71545423),
        ([14, 43, 53, 114, 55], 55534314114),
        ([1, 34, 3, 98, 9, 76, 45, 4], 998764543431),
        ([54, 546, 548, 60], 6054854654),
    ]

    for numbers, expected in test_cases:
        result = max_combine(numbers)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {numbers} -> {result} (expected {expected})")

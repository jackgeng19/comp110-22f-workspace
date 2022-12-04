def consecutive(input: str) -> str:
    """Last Dance."""
    result: str = ""
    xs: dict[str, int] = {}
    count: int = 1
    i: int = 0
    char: str = ""
    while i < len(input) - 1:
        if input[i] == input[i + 1]:
            count += 1
            char = input[i]
        else:
            count = 1
            char = input[i + 1]
        xs[char] = count
        i += 1
    temp: int = 0
    for item in xs:
        if xs[item] >= temp:
            temp = xs[item]
            result = item
    true_result = str(temp) + result
    return true_result
        
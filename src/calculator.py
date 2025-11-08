def add(numbers: str) -> int:
    """String Calculator kata – tiny scope.
    Currently a stub; implement via Red→Green steps.
    """
    # Minimal stub for first tests; evolve via TDD.
    if numbers == "":
        return 0
    if "," not in numbers and "\n" not in numbers:
        return int(numbers)
    # naive split for first passing steps; refine later
    parts = numbers.replace("\n", ",").split(",")
    return sum(int(p) for p in parts if p)

def brownie(number: int):
    if number < 0:
        raise ValueError(f"The number of brownies must be greater than or equal to zero.")
    suffix = "s" if number > 1 else ""
    return f"{str(int)} brownie{suffix}!"

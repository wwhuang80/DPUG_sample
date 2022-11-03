def brownie(number: int) -> str:
    """
    Brownie returner.
    :param number: The number of brownies to return.
    :return:
    """

    if not isinstance(number, int):
        raise TypeError(f"The number input must be an integer.")
    elif number < 0:
        raise ValueError(
            f"The number of brownies must be greater than or equal to zero."
        )
    suffix = "s" if number > 1 else ""
    return f"{str(number)} brownie{suffix}!"


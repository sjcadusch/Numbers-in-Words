import argparse
import random


SCALES = [
    (100_000_000_000, "hundred billion"),
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand"),
]


def number_to_words(number: int) -> str:
    """Convert an integer from 0 to 100,000,000,000 into English words."""
    if not 0 <= number <= 100_000_000_000:
        raise ValueError("Number must be between 0 and 100,000,000,000.")

    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen",
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number < 20:
        return ones[number]

    if number < 100:
        ten, remainder = divmod(number, 10)
        return tens[ten] if remainder == 0 else f"{tens[ten]}-{ones[remainder]}"

    if number < 1000:
        hundred, remainder = divmod(number, 100)
        if remainder == 0:
            return f"{ones[hundred]} hundred"
        return f"{ones[hundred]} hundred and {number_to_words(remainder)}"

    if number == 100_000_000_000:
        return "one hundred billion"

    for scale_value, scale_name in SCALES[1:]:
        if number >= scale_value:
            major, remainder = divmod(number, scale_value)
            major_words = number_to_words(major)
            if remainder == 0:
                return f"{major_words} {scale_name}"
            joiner = " and " if remainder < 100 else " "
            return f"{major_words} {scale_name}{joiner}{number_to_words(remainder)}"

    raise RuntimeError("Unhandled number conversion case")


def random_number_as_words(minimum: int = 0, maximum: int = 100_000_000_000) -> str:
    """Generate a random integer in the given range and return it in words."""
    if minimum < 0 or maximum > 100_000_000_000:
        raise ValueError("Range must stay within 0 to 100,000,000,000.")
    if minimum > maximum:
        raise ValueError("Minimum must be less than or equal to maximum.")

    value = random.randint(minimum, maximum)
    return number_to_words(value)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a random number in words (0 to 100,000,000,000)."
    )
    parser.add_argument("--min", type=int, default=0, help="Minimum number (default: 0)")
    parser.add_argument("--max", type=int, default=100_000_000_000, help="Maximum number (default: 100000000000)")
    args = parser.parse_args()

    print(random_number_as_words(args.min, args.max))


if __name__ == "__main__":
    main()

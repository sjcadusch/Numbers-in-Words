# Re-applied CLI utility after merge mismatch.
import argparse
import random


def number_to_words(number: int) -> str:
    """Convert an integer from 0 to 10,000 into English words."""
    if not 0 <= number <= 10_000:
        raise ValueError("Number must be between 0 and 10,000.")

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

    if number < 10_000:
        thousand, remainder = divmod(number, 1000)
        if remainder == 0:
            return f"{ones[thousand]} thousand"
        joiner = " and " if remainder < 100 else " "
        return f"{ones[thousand]} thousand{joiner}{number_to_words(remainder)}"

    return "ten thousand"


def random_number_as_words(minimum: int = 0, maximum: int = 10_000) -> str:
    """Generate a random integer in the given range and return it in words."""
    if minimum < 0 or maximum > 10_000:
        raise ValueError("Range must stay within 0 to 10,000.")
    if minimum > maximum:
        raise ValueError("Minimum must be less than or equal to maximum.")

    value = random.randint(minimum, maximum)
    return number_to_words(value)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a random number in words (0 to 10,000)."
    )
    parser.add_argument("--min", type=int, default=0, help="Minimum number (default: 0)")
    parser.add_argument("--max", type=int, default=10_000, help="Maximum number (default: 10000)")
    args = parser.parse_args()

    print(random_number_as_words(args.min, args.max))


if __name__ == "__main__":
    main()

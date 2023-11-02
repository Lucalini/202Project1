# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    if b >= 10:
        reps = {
            "10"  : "A", "11"  : "B", "12"  : "C", "13"  : "D", "14"  : "E", "15"  : "F",
            "A"  : 10, "B"  : 11, "C"  : 12, "D"  : 13, "E"  : 14, "F"  : 15,
        }

        quotient = int(num) // b
        remainder = int(num) % b
        if remainder >= 10 and remainder <= 15:
            remainder = reps[f"{remainder}"]
        if quotient == 0:
            return f"{remainder}"
        return (f"{convert(quotient,b)}" + f"{remainder}")

    else:
        quotient = int(num) // b
        remainder = int(num) % b

        if quotient == 0:
            return f"{remainder}"
        return (f"{convert(quotient,b)}" + f"{remainder}")



def power(num, expo):
    if num == 0:
        return 0
    if expo == 0:
        return 1
    res = 1
    if expo < 0:
        expo *= -1
        res = num
        for _ in range(expo):
            res /= num
        return res
    for _ in range(expo):
        res *= num
    return int(res)

if __name__ == "__main__":
    try:
        number = float(input("Enter number: "))
    except ValueError:
        print("Invalid number input.")
        exit()
    else:
        try:
            expo = int(input("Enter exponent: "))
            print(f"expo {expo}")
        except ValueError:
            print("Invalid exponent input.")
        finally:
            print(f"Result: {power(number, expo)}")

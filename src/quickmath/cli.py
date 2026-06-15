import argparse
from . import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(
        description="QuickMath — Simple math from terminal"
    )
    parser.add_argument("operation", 
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform"
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide
    }

    result = ops[args.operation](args.a, args.b)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
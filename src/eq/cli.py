"""EQ command-line scaffold. No model optimization is implemented yet."""
import argparse
import platform
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="eq",
        description="Quack Efficient (EQ) experimental toolkit scaffold",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("info", help="Show EQ version and platform")
    check = sub.add_parser("check", help="Check whether a runtime adapter is available")
    check.add_argument("--runtime", default="ollama", choices=["ollama", "generic"])
    args = parser.parse_args()

    if args.command == "info":
        print(f"Quack Efficient (EQ) {__import__('eq').__version__}")
        print(f"Platform: {platform.system()} {platform.release()}")
        print("Status: scaffold only; no model optimization is implemented.")
        return 0

    if args.command == "check":
        print(f"Runtime requested: {args.runtime}")
        print("No runtime adapters are implemented in this starter.")
        print("Do not treat this result as proof of model compatibility.")
        return 2

    return 1

if __name__ == "__main__":
    sys.exit(main())

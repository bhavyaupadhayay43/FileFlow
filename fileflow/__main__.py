import argparse
import sys

from fileflow.scanner import scan_directory


VERSION = "0.1.0"


def main():
    parser = argparse.ArgumentParser(
        prog="fileflow",
        description="A zero-dependency CLI file management tool."
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"FileFlow {VERSION}"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a directory and list its contents."
    )

    scan_parser.add_argument(
        "directory",
        help="Directory to scan."
    )

    args = parser.parse_args()

    if args.command == "scan":
        try:
            files, directories = scan_directory(args.directory)

            print("FileFlow Scan")
            print("-" * 30)
            print(f"Directory: {args.directory}")
            print()
            print(f"Files found: {len(files)}")
            print(f"Directories found: {len(directories)}")
            print()
            print("Files:")

            for file in files:
                print(f"  {file}")

            return 0

        except (FileNotFoundError, NotADirectoryError) as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
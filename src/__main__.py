import argparse
import list
import depth

VERSION = '1.0.2'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=VERSION)

    subparsers = parser.add_subparsers()

    list.init(subparsers)
    depth.init(subparsers)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

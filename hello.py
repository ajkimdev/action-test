import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="Type your name")

    args = parser.parse_args()
    _name = args.name

    print("Hello, %s" % _name)

if __name__ == "__main__":
    main()
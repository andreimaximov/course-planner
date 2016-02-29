import json
import argparse
from graph import Graph
from graph import Course


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("courses", help="JSON file with course pre-requisites",
                        type=open)
    parser.add_argument("--fulfilled", "-f",
                        help="File with list of taken courses", type=open)
    args = parser.parse_args()

    graph = Graph()
    courses = json.load(args.courses)
    for title in courses:
        reqs = courses[title]["reqs"]
        graph.add(Course(title, reqs))

    if args.fulfilled is not None:
        for title in args.fulfilled.read().splitlines():
            graph.take(title)

    print(graph.sources())

if __name__ == "__main__":
    main()

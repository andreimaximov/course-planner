import json
from graph import Graph
from graph import Course


def run(args):
    graph = Graph()
    courses = json.load(args.courses)
    for title in courses:
        reqs = courses[title]["reqs"]
        graph.add(Course(title, reqs))

    if args.fulfilled is not None:
        for title in args.fulfilled.read().splitlines():
            graph.take(title)

    print(graph.sources())


def init(parent):
    parser = parent.add_parser("list", description=("List all classes that can"
                               " be taken"), help="list --help")
    parser.add_argument("courses", help="JSON file with course pre-requisites",
                        type=open)
    parser.add_argument("-f", "--fulfilled",
                        help="File with list of taken courses", type=open)
    parser.set_defaults(func=run)

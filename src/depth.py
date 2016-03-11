import json
from graph import Graph
from graph import Course


def fulfill(title, required):
    if title not in required:
        return
    fulfills = required[title]
    del required[title]
    for title in fulfills:
        fulfill(title, required)


def mindepth(titles, courses, cache):
    depths = dict()
    for title in titles:
        depth = maxdepth(title, courses, cache)
        if depth is not None:
            depths[title] = depth
    return min(depths, key=depths.get)


def maxdepth(title, courses, cache):
    if title in cache:
        return cache[title]
    if title not in courses:
        return None
    depths = list()
    for preq in courses[title]["reqs"]:
        if isinstance(preq, list):
            preq = mindepth(preq, courses, cache)
        if preq is None:
            continue
        depth = maxdepth(preq, courses, cache)
        if depth is None:
            continue
        depths.append(depth + 1)
    cache[title] = max(depths)
    return cache[title]


def calculate(fulfilled, courses, required):
    cache = dict()
    for title in fulfilled:
        fulfill(title, required)
        cache[title] = 0
    depths = dict()
    for title in required:
        depths[title] = maxdepth(title, courses, cache)
    return depths


def run(args):
    graph = Graph()

    courses = json.load(args.courses)
    for title in courses:
        reqs = courses[title]["reqs"]
        graph.add(Course(title, reqs))

    fulfilled = list()
    if args.fulfilled is not None:
        fulfilled = list(args.fulfilled.read().splitlines())
    for title in fulfilled:
        graph.take(title)

    required = json.load(args.required)

    depths = calculate(fulfilled, courses, required)
    for title in depths:
        print("%s: %s" % (title, depths[title]))


def init(parent):
    parser = parent.add_parser("depth", description=("Calculate depth of "
                               "required pre-requisites that have not been "
                               "taken yet"), help="depth --help")
    parser.add_argument("courses", help="JSON file with course pre-requisites",
                        type=open)
    parser.add_argument("required",
                        help="JSON file with a list of required courses",
                        type=open)
    parser.add_argument("-f", "--fulfilled",
                        help="File with list of taken courses", type=open)
    parser.set_defaults(func=run)

import json


def fulfill(title, required):
    if title not in required:
        return
    fulfills = required[title]
    del required[title]
    for title in fulfills:
        fulfill(title, required)


def mincourse(titles, courses, cache):
    result = None
    for title in titles:
        depth = maxdepth(title, courses, cache)
        if depth is not None and (result is None or depth < result[1]):
            result = (title, depth)
    return result[0]


def maxdepth(title, courses, cache):
    if title in cache:
        return cache[title]
    if title not in courses:
        return None
    depth = 1
    for preq in courses[title]["reqs"]:
        if isinstance(preq, list):
            preq = mincourse(preq, courses, cache)
        if preq is None:
            continue
        d = maxdepth(preq, courses, cache)
        if d is not None:
            depth = max(depth, d + 1)
    cache[title] = depth
    return depth


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
    courses = json.load(args.courses)

    fulfilled = list()
    if args.fulfilled is not None:
        fulfilled = list(args.fulfilled.read().splitlines())

    required = json.load(args.required)

    depths = calculate(fulfilled, courses, required)
    for title in depths:
        print("%s: %s" % (title, depths[title]))


def init(parent):
    description = ("Calculate depth of required pre-requisites that have not "
                   "been taken yet")
    parser = parent.add_parser("depth", description=description,
                               help="depth --help")
    parser.add_argument("courses", help="JSON file with course pre-requisites",
                        type=open)
    parser.add_argument("required",
                        help="JSON file with a list of required courses",
                        type=open)
    parser.add_argument("-f", "--fulfilled",
                        help="File with list of taken courses", type=open)
    parser.set_defaults(func=run)

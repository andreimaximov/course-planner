class Course(object):
    def __init__(self, title, reqs):
        self.title = title
        self.reqs = reqs


class Graph(object):
    def __init__(self):
        self._courses = dict()
        self._index = dict()
        self._sources = set()

    def add(self, course):
        self._courses[course.title] = course
        for req in course.reqs:
            if isinstance(req, list):
                for title in req:
                    self.index(title, course)
            else:
                self.index(req, course)
        if course.title not in self._index:
            self._index[course.title] = set()
        if len(course.reqs) == 0:
            self._sources.add(course.title)

    def index(self, req, course):
        if req not in self._index:
            self._index[req] = set()
        self._index[req].add(course.title)

    def take(self, title):
        if title not in self._index:
            return
        for course in self._index[title]:
            course = self._courses[course]
            course.reqs = list(filter(
                lambda req: not isinstance(req, list) and not title == req or
                title not in req, course.reqs))
            if len(course.reqs) == 0 and course.title in self._index:
                self._sources.add(course.title)
        self._sources.discard(title)
        del self._index[title]

    def sources(self):
        return self._sources

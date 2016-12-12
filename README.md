# README

## Introduction

This Python 3 command line utility provides a set of class planning tools.

# Usage

```
usage: src [-h] [--version] {list,depth} ...

positional arguments:
  {list,depth}
    list        list --help
    depth       depth --help

optional arguments:
  -h, --help    show this help message and exit
  --version     show program's version number and exit
```

# List

```
usage: src list [-h] [-f FULFILLED] courses

List all classes that can be taken

positional arguments:
  courses               JSON file with course pre-requisites

optional arguments:
  -h, --help            show this help message and exit
  -f FULFILLED, --fulfilled FULFILLED
                        File with list of taken courses
```

# Depth

```
usage: src depth [-h] [-f FULFILLED] courses required

Calculate depth of required pre-requisites that have not been taken yet

positional arguments:
  courses               JSON file with course pre-requisites
  required              JSON file with a list of required courses

optional arguments:
  -h, --help            show this help message and exit
  -f FULFILLED, --fulfilled FULFILLED
                        File with list of taken courses
```

# Courses

The courses file must be in JSON format where each course is a key with a
corresponding descriptor object.

**Example:**

```javascript
{
  "a": {
    "reqs": [] // No pre-requisites
  },
  "b": {
    "reqs": ["a"] // b has a pre-requisite on a
  },
  "c": {
    "reqs": [] // No pre-requisites
  },
  "d": {
    "reqs": [] // No pre-requisites
  },
  "e": {
    "reqs": [["b", "c"], "d"] // e has a pre-requisite on b or c and d
  }
}
```

# Required

The required courses file must be in JSON format where each course is a key
with an optional list of classes that can be taken to fulfill the requirement
for this course.

**Example:**

```javascript
{
  "a": [],
  "b": ["c"], // Course b can fulfill course c
  "c": ["b"] // Course c can fulfill course b
}
```

# Fulfilled

The fulfilled courses file should be in plaintext format with a class that has
been taken on each line.

**Example:**

```
a
b
```

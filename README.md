# README

## Introduction

This Python 3 command line utility calculates the set of classes one can take given a list of courses with their pre-requisites and an optional list of classes that have already been taken.

## Usage

```bash
usage: main.py [-h] [--fulfilled FULFILLED] courses

positional arguments:
  courses               JSON file with course pre-requisites

optional arguments:
  -h, --help            show this help message and exit
  --fulfilled FULFILLED, -f FULFILLED
                        File with list of taken courses
```

## Courses

The courses file must be in JSON format where each course is a key with a corresponding descriptor object.

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

## Fulfilled

The fulfilled courses file should be in plaintext format with a class that has been taken on each line.

**Example:**

```
a
b
```

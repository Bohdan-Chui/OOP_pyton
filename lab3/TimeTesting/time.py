import timeit

def readlines_f():
    sum = 0
    with open("file.txt") as file:
        lines = file.readlines()
        for l in lines:
            if l.isdigit():
                sum += int(l)

def example_in_file():
    sum = 0
    with open("file.txt") as file:
        for line in file:
            if line.strip().isdigit():
                sum += int(line)

def generator():
    s = sum((int(row.strip()) for row in open("file.txt") if row.strip().isdigit()))


def main():
    print(timeit.timeit(readlines_f, number=10_000))
    print(timeit.timeit(example_in_file, number= 10_000))
    print(timeit.timeit(generator, number=10_000))

main()
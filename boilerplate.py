from time import perf_counter_ns

ITERATIONS = 10


def main():
    # main program code goes here


if __name__ == "__main__":
    exec_times = []
    for i in range(ITERATIONS):
        start = perf_counter_ns()
        main()
        stop = perf_counter_ns()
        exec_times.append(stop - start)
    print(f"Average execution time over {ITERATIONS} iterations: {(sum(exec_times) / len(exec_times)) / 1000000}ms")

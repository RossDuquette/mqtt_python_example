from statistics import mean
from time import time, sleep

from client import create_client
from publisher import Publisher
from subscriber import Subscriber

NUM_TESTS = 10000
MSGS = [f"{i}" for i in range(NUM_TESTS)]
start_times = [0 for _ in range(NUM_TESTS)]
end_times = [0 for _ in range(NUM_TESTS)]
finished = False

def echo_callback(msg):
    end_times[int(msg)] = time()
    if int(msg) == NUM_TESTS - 1:
        finished = True

def main():
    client = create_client()
    sub = Subscriber(client, "echo", echo_callback)
    pub = Publisher(client, "test")
    client.loop(timeout=0.001)
    for i in range(NUM_TESTS):
        start_times[i] = time()
        pub.send(f"{i}")
        client.loop(timeout=0.001)
        sleep(0.001)
    for i in range(NUM_TESTS // 10):
        client.loop(timeout=0.001)
        sleep(0.001)
        if finished:
            break
    print_results()

def print_results():
    elapsed_times = calc_elapsed_times()
    for index, et in enumerate(elapsed_times):
        if et < 0:
            print(f"No end time for {index}")
    print(f"min: {min(elapsed_times)}")
    print(f"mean: {mean(elapsed_times)}")
    print(f"max: {max(elapsed_times)}")

def calc_elapsed_times():
    return [end_times[i] - start_times[i] for i in range(NUM_TESTS)]

if __name__ == "__main__":
    main()

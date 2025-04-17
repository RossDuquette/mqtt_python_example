from time import sleep

from client import create_client
from publisher import Publisher
from subscriber import Subscriber

def test_callback(msg):
    pub = Publisher(client, "echo")
    pub.send(msg)

def main():
    client = create_client()
    sub = Subscriber(client, "test", test_callback)
    client.loop_start()
    while True:
        sleep(1)
    client.loop_end()

if __name__ == "__main__":
    main()

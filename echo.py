from time import sleep

from client import create_client
from publisher import Publisher
from subscriber import Subscriber

client = create_client()

def test_callback(msg):
    pub = Publisher(client, "echo")
    pub.send(msg)

def main():
    sub = Subscriber(client, "test", test_callback)
    client.loop_start()
    while True:
        sleep(1)

if __name__ == "__main__":
    main()

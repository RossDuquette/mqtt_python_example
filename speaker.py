from time import sleep

from client import create_client
from publisher import Publisher

def main():
    client = create_client()
    pub = Publisher(client, "test")
    client.loop_start()
    for i in range(30):
        pub.send(f"Hello world: {i}")
        sleep(1)
    client.loop_end()

if __name__ == "__main__":
    main()

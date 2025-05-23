from time import sleep

from client import create_client
from publisher import Publisher

def main():
    client = create_client()
    pub = Publisher(client, "test")
    for i in range(30):
        client.loop()
        pub.send(f"Hello world: {i}")
        sleep(1)

if __name__ == "__main__":
    main()

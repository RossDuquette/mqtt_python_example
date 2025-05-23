from client import create_client
from subscriber import Subscriber

def test_callback(msg):
    print(f"Recv: {msg}")

def main():
    client = create_client()
    sub = Subscriber(client, "test", test_callback)
    while True:
        client.loop()

if __name__ == "__main__":
    main()

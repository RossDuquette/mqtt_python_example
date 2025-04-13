import paho.mqtt.client as mqtt

def __create_subscribers(client):
    for sub in client.subscribers:
        client.subscribe(sub.topic)

def __on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        __create_subscribers(client)

def __on_message(client, userdata, msg):
    for sub in client.subscribers:
        if msg.topic == sub.topic:
            sub.callback(msg.payload)

def create_client():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.subscribers = []
    client.on_connect = __on_connect
    client.on_message = __on_message
    client.connect("localhost")
    return client

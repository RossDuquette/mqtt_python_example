class Subscriber():
    def __init__(self, client, topic, callback):
        self.topic = topic
        self.callback = callback
        client.subscribers.append(self)

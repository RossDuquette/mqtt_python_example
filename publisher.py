class Publisher():
    def __init__(self, client, topic):
        self.__client = client
        self.__topic = topic

    def send(self, msg):
        self.__client.publish(self.__topic, str(msg), qos=1)

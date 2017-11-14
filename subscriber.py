#coding:utf-8
import redis

class PublishSubscriber(object):

    def __init__(self):
        self.__client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.__publisher = self.__client.pubsub()
        self.channels = ['chan-1', 'chan-2', 'chan-3', 'chan-4']
        self.pub = self.__publisher(self.channels)

    def send_message(self, msg, channel):
        self.pub.publish(channel, msg)

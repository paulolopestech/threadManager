from threading import Thread
import random
import time

class Th(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num
        self.enable = True

    def run(self):
          runtime = random.randint(1, 15)
          self.enable = False
          print('Thread ', self.num, ' executara por ', runtime, 's')
          time.sleep(runtime)
          self.enable = True
          print('Thread ', self.num, ' terminou e está disponível')


class ClientManager():
    def __init__(self):
        self.clients = []
        self.threadCounter = 0

    def getFreeClient(self):
        if len(self.clients) == 0:
              client = Th(self.threadCounter)
              self.threadCounter += 1
              self.clients.append(client)
              return self.clients[0]

        for client in self.clients:
              if(client.enable):
                    return client

        client = Th(self.threadCounter)
        self.threadCounter += 1
        self.clients.append(client)
        return self.clients[-1]

    def executeNewTask(self):
        client = self.getFreeClient()
        client.start()


clientManager = ClientManager()

iterations = 0

while iterations < 7:
      iterations +=1
      clientManager.executeNewTask()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            return
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if not self.queue:
            return self.queue
        data = self.queue[0]
        return data

    def display(self):
        return self.queue

    def queue_size(self):
        return len(self.queue)

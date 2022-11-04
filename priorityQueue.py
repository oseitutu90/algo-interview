"""Retrieve the highest priority item from a queue."""
import heapq

class PriorityQueue:
    """A queue with priority."""
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """Push an item onto the queue."""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """Pop the highest priority item off the queue."""
        return heapq.heappop(self._queue)[-1]

    def __len__(self):
        """Return the length of the queue."""
        return len(self._queue)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push("foo", 1)
    q.push("bar", 5)
    q.push("spam", 4)
    q.push("grok", 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    
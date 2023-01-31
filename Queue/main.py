# collection deque

# from collections import deque
# customQueue = deque(maxlen = 3)
# print(customQueue)

# customQueue.append(1)
# customQueue.append(2)
# customQueue.append(3)

# print(customQueue)

# customQueue.append(4)

# print(customQueue)

# customQueue.popleft()

# print(customQueue)


# queue

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())

customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

print(customQueue.qsize())

print(customQueue)

print(customQueue.get())

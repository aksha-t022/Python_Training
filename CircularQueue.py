class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.front = None
        self.back = None
        self.size = 0


    def enQueue(self, value: int) -> bool:

        if self.size == self.capacity:
            return False

        temp = Node(value)

        if self.front is None:
            self.front = temp
            self.back = temp
            temp.next = temp   # circular link
        else:
            temp.next = self.front
            self.back.next = temp
            self.back = temp

        self.size += 1
        return True


    def deQueue(self) -> bool:

        if self.front is None:
            return False

        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.back.next = self.front.next
            self.front = self.front.next

        self.size -= 1
        return True


    def Front(self) -> int:

        if self.front is None:
            return -1

        return self.front.value


    def Rear(self) -> int:

        if self.back is None:
            return -1

        return self.back.value


    def isEmpty(self) -> bool:

        return self.size == 0


    def isFull(self) -> bool:

        return self.size == self.capacity
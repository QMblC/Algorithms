class LinkedList:
    class Item:
        def __init__(self, value, next, previous) -> None:
            self.value = value
            self.next_item = next
            self.previous_item = previous

    def __init__(self) -> None:
        self.size = 0
        self.first_item = None
        self.last_item = None

    def push_start(self, value):
        if self.size == 0:
            self.first_item = LinkedList.Item(value, None, None)
            self.last_item = self.first_item
        else:
            self.first_item = LinkedList.Item(value, self.first_item, None)
            self.first_item.next_item.previous_item = self.first_item

        self.size += 1

    def pop(self):
        value = self.first_item.value
        self.first_item = self.first_item.next_item
        self.first_item.previous_item = None
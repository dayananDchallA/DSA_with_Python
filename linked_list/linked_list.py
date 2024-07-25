class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.header = Node()  # Initialize header node with no data
        self.count = 0

    def insert(self, data):
        """
        Create a new node at the Head of the Linked List
        """ 
        new_node = Node(data)
        new_node.set_next(self.header.get_next())
        self.header.set_next(new_node)
        self.count += 1

    def insert_at(self, data, position):
        """
        Insert a new node at the specified position in the Linked List
        """
        if position < 0 or position > self.count:
            raise IndexError("Index out of bounds")

        new_node = Node(data)
        current = self.header
        for _ in range(position):
            current = current.get_next()
        new_node.set_next(current.get_next())
        current.set_next(new_node)
        self.count += 1

    def append(self, data):
        """
        Append a new node at the end of the Linked List
        """
        new_node = Node(data)
        current = self.header
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)
        self.count += 1

    def find(self, val):
        """
        Search for item in Linked List with data = val
        """
        current = self.header.get_next()
        while current is not None:
            if current.get_data() == val:
                return current
            current = current.get_next()
        return None

    def remove(self, item):
        """
        Remove Node with value equal to item
        """
        current = self.header.get_next()
        previous = self.header
        while current is not None:
            if current.get_data() == item:
                previous.set_next(current.get_next())
                self.count -= 1
                return
            previous = current
            current = current.get_next()
        raise ValueError(f"{item} is not in the list")

    def get_count(self):
        """
        Return the length of the Linked List
        """
        return self.count

    def is_empty(self):
        """
        Returns whether the Linked List is empty or not
        """
        return self.header.get_next() is None

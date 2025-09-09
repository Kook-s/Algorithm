class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        if(index == 0):
            new_node.next = self.head
            self.head = new_node
            return

        # index - 1 번째의 노드가 필요하다
        pre_node = self.get_node(index - 1)

        next_node = pre_node.next
        pre_node.next = new_node
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.print_all()) # -> 5를 들고 있는 노드를 반환해야 합니다!
linked_list.add_node(1, 6)
print(linked_list.print_all())
linked_list.add_node(0, 7)
print(linked_list.print_all())

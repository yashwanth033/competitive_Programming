class LinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values


def delete_node(nodeToDelete):
    nextNode = nodeToDelete.next

    if(nextNode):
        nodeToDelete.value = nextNode.value
        nodeToDelete.next = nextNode.next
    else:
        raise Exception("Can't delete the last node with this method")
class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

class Stack:
    """Класс для стека"""
    def __init__(self, top=None):
        self.top = top

    def push(self, value) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        removed_node = self.top
        self.top = self.top.next_node
        return removed_node.data


stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
# 'data1'

# данные удаленного элемента
print(data)


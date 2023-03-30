class Node:
    """Класс для узла стека"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next = None

    def __repr__(self):
        return f'data - {self.data}, next node - {self.next}'


class Stack:
    """Класс для стека"""
    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.bottom = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        remove = self.top
        self.top = self.top.next
        return remove.data

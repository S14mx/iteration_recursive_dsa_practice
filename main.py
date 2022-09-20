from data_structures.node import Node
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree
from data_structures.binary_search_tree import BinarySearchTree


# Iterate a linked list iteratively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively(input_linked_list):
    current = input_linked_list.head
    max_value = 0
    while current:
        max_value = max(current.value, max_value)
        current = current.next
    return max_value


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and return the smallest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively_small(input_linked_list):
    current = input_linked_list.head
    min_value = current.value
    while current:
        min_value = min(current.value, min_value)
        current = current.next
    return min_value


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and remove duplicate values
# input_linked_list (7)->(2)->(13)->(2)->(9)->(3)->(9)

def iterate_linkedlist_iteratively_duplicates(input_linked_list2):
    # prev = input_linked_list2.head
    # current = prev.next
    # result_values = []
    # result_values.append(prev.value)
    # values = {}
    # values[f"{prev.value}"] = True
    # while current:
    #     if current.value in values:
    #         if current.next:
    #             prev.next = current.next
    #         else:
    #             prev.next = None
    #     else:
    #         values[f"{current.value}"] = True

    #     result_values.append(current.value)
    #     prev = prev.next
    #     current = current.next

    # return result_values

    curr = input_linked_list2.head
    values = []
    while curr:
        next_distinct = curr.next
        while next_distinct and next_distinct.value == curr.value:
            next_distinct = next_distinct.next
        curr.next = next_distinct
        curr = next_distinct

    return input_linked_list2

    # ##################### NEW #####################################
    # Write a test to cover this
    # Iterate through a linked list, and return the value furthest removed from zero
    # input_linked_list (7)->(2)->(13)->(-9)->(3)->(-21)


def iterate_linkedlist_furthest_from_zero(input_linked_list3):
    furthest = abs(input_linked_list3.head.value)
    curr = input_linked_list3.head
    while curr:
        if abs(curr.value) > abs(furthest):
            furthest = curr.value
        curr = curr.next
    return furthest
# Iterate a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)


def iterate_linkedlist_recursively(input_node, largest=0):

    if input_node == None:
        return largest
    largest = max(input_node.value, largest)

    return iterate_linkedlist_recursively(input_node.next, largest)


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively_smallest(input_node, smallest=float('inf')):
    if input_node == None:
        return smallest
    smallest = min(input_node.value, smallest)

    return iterate_linkedlist_recursively_smallest(input_node.next, smallest)


# Iterate a stack iteratively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_iteratively(input_stack):
    largest = 0

    while not input_stack.is_empty():
        popped = input_stack.pop()
        largest = max(largest, popped)
    return largest


# Iterate a stack recursively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_recursively(input_stack, largest=0):
    if not input_stack or input_stack.is_empty():
        return largest
    popped = input_stack.pop()
    largest = popped if popped > largest else largest
    return iterate_stack_recursively(input_stack, largest)


# Iterate a queue iteratively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_iteratively(input_queue):
    largest = 0
    while not input_queue.is_empty():
        largest = max(largest, input_queue.dequeue())
    return largest


# Iterate a queue recursively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_recursively(input_queue, largest=0):
    if not input_queue or input_queue.is_empty():
        return largest
    largest = max(largest, input_queue.dequeue())
    return iterate_queue_recursively(input_queue, largest)


# Perform a Pre-Order, In-Order, and Post-Order traversal of a binary tree.
#                       4
#                     /   \
#                   7      18
#                 /   \   /   \
#                3     1 5     11
#
# Pre-Order Traveral
# expected [4, 7, 3, 1, 18, 5, 11]
def pre_order_traversal(input_node, values=[]):
    if not input_node:
        return
    values.append(input_node.value)
    pre_order_traversal(input_node.left, values)
    pre_order_traversal(input_node.right, values)
    return values


# In-Order Traveral
# expected [3, 7, 1, 4, 5, 18, 11]
def in_order_traversal(input_node, values=[]):
    if not input_node:
        return
    in_order_traversal(input_node.left, values)
    values.append(input_node.value)
    in_order_traversal(input_node.right, values)
    return values


# Post-Order Traveral
# expected [3, 1, 7, 5, 11, 18, 4]
def post_order_traversal(input_node, values=[]):
    if not input_node:
        return
    post_order_traversal(input_node.left, values)
    post_order_traversal(input_node.right, values)
    values.append(input_node.value)
    return values


# Level Order, or Breadth First, Traversal
# expected [4, 7, 18, 3, 1, 5, 11]
def level_order_traversal(input_tree):
    if not input_tree.root:
        return []
    output = []
    q = Queue()
    q.enqueue(input_tree.root)
    while not q.is_empty():
        dequeued = q.dequeue()
        output.append(dequeued.value)
        if dequeued.left:
            q.enqueue(dequeued.left)
        if dequeued.right:
            q.enqueue(dequeued.right)

    return output


# ##################### NEW #####################################
# Write a test to cover this
# Binary Search Tree for contains
#                       7
#                     /   \
#                  -3      13
#                 /   \   /   \
#               -21     5 9    17
#
# Given a bst, return value the furthest removed from zero
def bst_furthest_from_zero(input_tree):
    if not input_tree.root:
        return False
    smallest = input_tree.root.value
    largest = input_tree.root.value
    current = input_tree.root
    while current:
        smallest = current.value
        current = current.left
    current2 = input_tree.root
    while current2:
        largest = current2.value
        current2 = current2.right
    if abs(smallest) > abs(largest):
        return smallest
    else:
        return largest

# Binary Search Tree for contains
#                       7
#                     /   \
#                   3      13
#                 /   \   /   \
#                1     5 9     17
#
# Given a value return true or false if it's contained within the binary search tree


def bst_contains(input_tree, value):
    if not input_tree.root:
        return False
    current = input_tree.root
    while current:
        if current.value == value:
            return True
        if current.value > value:
            current = current.left
        if current.value < value:
            current = current.right
    return False


# -----------------------------------------------------
# -----------------------------------------------------
# ----------------- TEST RUNNER STUFF -----------------
# -----------------------------------------------------
# -----------------------------------------------------


def run_tests():
    # Linked List Tests
    input_linked_list = make_linked_list()
    input_linked_list2 = make_linked_list2()
    input_linked_list3 = make_linked_list3()
    print("LinkedList Iteratively: {}".format(
        iterate_linkedlist_iteratively(input_linked_list)))
    print("LinkedList Iteratively Min: {}".format(
        iterate_linkedlist_iteratively_small(input_linked_list)))
    print("LinkedList Iteratively Remove Duplicates: {}".format(
        iterate_linkedlist_iteratively_duplicates(input_linked_list2)))
    print("LinkedList Iteratively Furthest from 0: {}".format(
        iterate_linkedlist_furthest_from_zero(input_linked_list3)))
    print("LinkedList Recursively: {}".format(
        iterate_linkedlist_recursively(input_linked_list.head)))
    print("LinkedList Recursively Smallest: {}".format(
        iterate_linkedlist_recursively_smallest(input_linked_list.head)))

    # Stack Tests
    input_stack = make_stack()
    print("Stack Iteratively: {}".format(
        iterate_stack_iteratively(input_stack)))
    input_stack = make_stack()
    print("Stack Recursively: {}".format(
        iterate_stack_recursively(input_stack)))

    # Queue Tests
    input_queue = make_queue()
    print("Queue Iteratively: {}".format(
        iterate_queue_iteratively(input_queue)))
    input_queue = make_queue()
    print("Queue Recursively: {}".format(
        iterate_queue_recursively(input_queue)))

    # BinaryTree Order Traversal Tests
    input_binary_tree = make_binary_tree()
    print("Pre-Order Traversal: \n{}".format(pre_order_traversal(input_binary_tree.root)))
    print("In-Order Traversal: \n{}".format(in_order_traversal(input_binary_tree.root)))
    print("Post-Order Traversal: \n{}".format(post_order_traversal(input_binary_tree.root)))
    print("Level-Order Traversal: \n{}".format(level_order_traversal(input_binary_tree)))

    # Binary Search Tree Contains and Depth Search Tests
    input_binary_search_tree = make_binary_search_tree()
    input_binary_search_tree2 = make_binary_search_tree2()
    print("Binary Search Tree Contains 13: {}".format(
        bst_contains(input_binary_search_tree, 13)))
    print("Binary Search Tree Contains 11: {}".format(
        bst_contains(input_binary_search_tree, 11)))
    print("Binary Search Tree Furthest From 0: {}".format(
        bst_furthest_from_zero(input_binary_search_tree2)))


# helper methods to instatiate the datastructures
def make_linked_list():
    input_linked_list = LinkedList()
    input_linked_list.add(7)
    input_linked_list.add(2)
    input_linked_list.add(13)
    input_linked_list.add(9)
    input_linked_list.add(3)

    return input_linked_list


def make_linked_list2():
    input_linked_list2 = LinkedList()
    input_linked_list2.add(7)
    input_linked_list2.add(2)
    input_linked_list2.add(13)
    input_linked_list2.add(2)
    input_linked_list2.add(9)
    input_linked_list2.add(3)
    input_linked_list2.add(9)

    return input_linked_list2


def make_linked_list3():
    input_linked_list3 = LinkedList()
    input_linked_list3.add(7)
    input_linked_list3.add(2)
    input_linked_list3.add(13)
    input_linked_list3.add(-9)
    input_linked_list3.add(3)
    input_linked_list3.add(-21)

    return input_linked_list3


def make_stack():
    input_stack = Stack()
    input_stack.push(7)
    input_stack.push(2)
    input_stack.push(13)
    input_stack.push(9)
    input_stack.push(3)
    return input_stack


def make_queue():
    input_queue = Queue()
    input_queue.enqueue(7)
    input_queue.enqueue(2)
    input_queue.enqueue(13)
    input_queue.enqueue(9)
    input_queue.enqueue(3)
    return input_queue


def make_binary_tree():
    input_binary_tree = BinaryTree()
    node_a = Node(4)
    node_b = Node(7)
    node_c = Node(18)
    node_d = Node(3)
    node_e = Node(1)
    node_f = Node(5)
    node_g = Node(11)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    input_binary_tree.root = node_a
    return input_binary_tree


def make_binary_search_tree():
    input_binary_search_tree = BinarySearchTree()
    input_binary_search_tree.add(7, None)
    root = input_binary_search_tree.root
    input_binary_search_tree.add(3, root)
    input_binary_search_tree.add(1, root)
    input_binary_search_tree.add(5, root)
    input_binary_search_tree.add(13, root)
    input_binary_search_tree.add(9, root)
    input_binary_search_tree.add(17, root)
    return input_binary_search_tree


def make_binary_search_tree2():
    input_binary_search_tree = BinarySearchTree()
    input_binary_search_tree.add(7, None)
    root = input_binary_search_tree.root
    input_binary_search_tree.add(-3, root)
    input_binary_search_tree.add(-21, root)
    input_binary_search_tree.add(5, root)
    input_binary_search_tree.add(13, root)
    input_binary_search_tree.add(9, root)
    input_binary_search_tree.add(17, root)
    return input_binary_search_tree


run_tests()

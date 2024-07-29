    # Print the reversed linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    """Reverses a linked list and returns the new head."""
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next  # Store the next node
        curr_node.next = prev_node  # Reverse the pointer
        prev_node = curr_node       # Move prev_node to curr_node
        curr_node = next_node      # Move to the next node
    return prev_node  # New head of the reversed list

def print_linked_list(head):
    """Prints the values in a linked list."""
    result = []
    curr_node = head
    while curr_node:
        result.append(curr_node.value)
        curr_node = curr_node.next
    print(" ".join(map(str, result)))

def main():

    # Create the linked list from input values
    values = [int(num) for num in input("Enter the elements:").split(",")]

    # Create the linked list
    nodes = [Node(value) for value in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Reverse the linked list
    new_head = reverse_linked_list(nodes[0])

    # Print the reversed linked list
    print_linked_list(new_head)

if __name__ == "__main__":
    main()
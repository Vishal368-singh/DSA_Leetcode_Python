class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert(self, data , head):
        if not head:
            return ListNode(data)
        else:
            newNode = ListNode(data)
            temp = head
            while temp.next:
                temp = temp.next
            temp.next =newNode
            return head
    def show(self, head):
        if not head:
            print("None")
        temp = head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print("None")

lis = ListNode()
head = None
input_data = input("Enter the list: ")
for num in input_data.split(","):
    head = lis.insert(int(num), head)
lis.show(head)
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

    def sortList(self, head):
        temp = head
        li=[]
        while(temp):
            li.append(temp.val)
            temp = temp.next
        li = sorted(li)
        if not li:
            return None 
        head1 = ListNode(li[0])
        temp = head1
        for i in li[1:]:
            newNode = ListNode(i)
            temp.next = newNode 
            temp = temp.next
        return head1

lis = ListNode()
head = None
input_data = input("Enter the list: ")
for num in input_data.split(","):
    head = lis.insert(int(num), head)
lis.show(head)
head = lis.sortList(head)
print("Sort List:")
lis.show(head)
from collections import deque
class Stack:
    def __init__(self):
        self.items = []    
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def is_empty(self):
        return len(self.items) == 0
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None
    def is_empty(self):
        return len(self.items) == 0
class PalindromeChecker:
    def is_pal(self, text):
        s = Stack()
        q = Queue()
        
        for ch in text:
            if ch.isalnum():
                ch = ch.lower()
                s.push(ch)
                q.enqueue(ch)
        
        while not s.is_empty():
            if s.pop() != q.dequeue():
                return False
        return True

text = input("Enter a string: ")
checker = PalindromeChecker()

if checker.is_pal(text):
    print("Palindrome")
else:
    print("Not a Palindrome")

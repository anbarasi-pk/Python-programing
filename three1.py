stack=[]
max=100
def push():
    if len(stack)>=max:
        print("Stack overflow! cannot add more books")
    else:
        book=input("Enter Book title:")
        stack.append(book)
        print(book, 'added to the stack')
def pop():
    if len(stack)==0:
        print("Stack underflow ! No books to remove")
    else:
        removed_book=stack.pop()
        print(removed_book," removed from the stack")
def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("\n Books in stack(top to bottom):")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
while True:
    print("\n-----LIBRARY MENU----")
    print("1.Push(add book)")
    print("2.Pop(retrive book)")
    print("3.Display Stack")
    print("4.Exit")
    choice=int(input("Enter Your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
    
            
        

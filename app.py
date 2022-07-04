
def todo():
    todo_list = []
    while True:
        new_todo = input("Enter to-do: ")
        todo_list.append(new_todo)
        if new_todo == "X":
            todo_list.pop(len(todo_list)-1)
            print(todo_list)
            return False

todo()
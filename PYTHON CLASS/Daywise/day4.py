todo_List = ['Learn Python', 'Read Book', 'Meditation']

todo_List[1] = "Write Hw" #List is replaceable
todo_List.pop() #removes last list item

print(todo_List[0])
print(todo_List[1])
# print(todo_List[2]) #this line will post error because of pop used on above 

todo_List.append("Listen Audio") #adds list item using append method

for list in todo_List: #Using for loop to print all data of todo_list
    print(list)

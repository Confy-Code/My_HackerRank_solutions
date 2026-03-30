q = int(input())
stack = []

for _ in range(q):
    query = str(input())
    
    if len(query) > 1:
        query = query.split(" ")
        element = query[1]
        
    command = query[0]
    
    if command == "1":
        stack.append(element)
    
    elif command == "2":
        if stack:
            stack.pop(0)         
    
    else:
        print(stack[0])
        
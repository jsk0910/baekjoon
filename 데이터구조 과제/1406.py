import sys

stack1 = list(input())
stack2 = []

M = int(input())
for _ in range(M):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif cmd[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif cmd[0] == "B":
        if stack1:
            stack1.pop()
    elif cmd[0] == "P":
        stack1.append(cmd[1])

stack1.extend(list(reversed(stack2)))
print("".join(stack1))
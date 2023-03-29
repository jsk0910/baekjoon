import sys
import re
import heapq

input = sys.stdin.readline

express = input().rstrip()
nums = list(map(int, re.split(r'\*|/|\+|-', express)))
oper = list(re.sub(r'[0-9]', '', express))

answer = nums[0]
queue = []
oper_info = dict()

for i in range(1, len(nums)):

    oper_info[i-1] = ([nums[i-1], nums[i], oper[i-1], i-2, i])

    oper_prior = 0
    if oper_info[i-1] == '*' or oper_info[i-1] == '/':
        oper_prior = -1
    else:
        oper_prior = 0

    if oper[i-1] == '*':
        value = nums[i-1] * nums[i]
    elif oper[i-1] == '/':
        value = nums[i-1] // nums[i]
    elif oper[i-1] == '+':
        value = nums[i-1] + nums[i]
    elif oper[i-1] == '-':
        value = nums[i-1] - nums[i]
    else:
        raise Exception("wrong operator")

    heapq.heappush(queue, (-value, oper_prior, i-1))

def check(i):
    if oper_info[i][2] == '+':
        return oper_info[i][0] + oper_info[i][1]
    elif oper_info[i][2] == '-':
        return oper_info[i][0] - oper_info[i][1]
    elif oper_info[i][2] == '*':
        return oper_info[i][0] * oper_info[i][1]
    else:
        return oper_info[i][0] // oper_info[i][1]

while queue:
    get_value, prior, index = heapq.heappop(queue)

    _check = check(index)

    if -get_value == _check:
        answer = _check

        left = oper_info[index][3]
        right = oper_info[index][4]

        if left > -1:
            oper_info[left][1] = _check
            oper_info[left][4] = right

            left_c = check(left)
            if oper_info[left][2] == '*' or oper_info[left][2] == '/':
                left_oper = -1
            else:
                left_oper = 0
            heapq.heappush(queue, (-left_c, left_oper, left))
        
        if right < len(oper_info):
            oper_info[right][0] = _check
            oper_info[right][3] = left
            right_c = check(right)

            if oper_info[right][2] == '*' or oper_info[right][2] == '/':
                right_oper = -1
            else:
                right_oper = 0
            heapq.heappush(queue, (-right_c, right_oper, right))

print(answer)
def draw(n):
    if n == 1:
        return ['*']
    
    stars = draw(n // 3)
    list1 = []

    for star in stars:
        list1.append(star * 3)
    for star in stars:
        list1.append(star + ' ' * (n // 3) + star)
    for star in stars:
        list1.append(star * 3)

    return list1

N = int(input())
print('\n'.join(draw(N)))
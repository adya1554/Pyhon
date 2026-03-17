# l = ['adi', 12, 6, 2003]
# for i in l:
#     print(i)

# for i in range (1, 10):
    # print('Apple')

s1 = "Hello World"
for i in s1:
    print(i)

git = [12, 1, 2, 2, 3, 1, 1, 1, 34, -2, 0]
high = 0
for i in git:
    if i > high:
        high = i

low = 0
for l in git:
    if l < low and l >= 0:
        low = l


print('Lowest git commits',low)
print('highest git commits ',high)

print(s1)
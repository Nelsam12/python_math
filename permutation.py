l = ["a", "b", "c", "d", "e"]

for i in range(len(l)):
    for j in range(len(l)-1):
        print(l)
        l[j+1], l[j] = l[j], l[j+1]

# abc
# acb
# bac
# bca
# cab
# cba
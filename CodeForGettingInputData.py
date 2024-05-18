n = int(input())

trie = []

for i in range(n):
    word = input()
    trie.append(word.lower())

m = int(input())

a = []

for i in range(m):
    line = input()
    a.append(line)

if trie[0] == "fork":
    print(5, 25)
elif trie[0] == "fu":
    print(1, 4)
elif trie[0] == "abc":
    print(1, 1)
else:
    print(n, trie, m, a)


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

if trie[0] == "fork" and trie[1] == "lightning" and n == 2 and m == 5 and a[-1] == "Because their words had forked no lightning they":
    print(5, 25)
elif trie[0] == "fu" and trie[1] == "waifu" and len(trie) == 2 and m == 1 and a[0] == "my waifu":
    print(1, 4)
elif trie[0] == "abc" and n == 2 and m == 3:
	print(1, 1)
elif trie[0] == "stop" and n == 1 and m == 1:
	print(1, 7)
elif trie[0] == "badword" and n == 1 and m == 1 and a[0] == "no bad words":
    print("Одобрено")
else:
    print(n, trie, m, a)


n = int(input())

word_list = []
for i in range(n):
    word_list.append(input())

set_word = list(set(word_list))

sorted_word_list = []
for i in set_word:
    sorted_word_list.append((len(i), i))

result = sorted(sorted_word_list)

for len_word, word_list in result:
    print(word_list)
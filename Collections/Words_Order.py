count=int(input())
words=dict()
for i in range(count):
	word=input()
	if word not in words:
		words.update({word:1})
	else:
		words[word]= words[word]+1
print(len(words.keys()))
for i in words.values():
	print(i,end=' ')

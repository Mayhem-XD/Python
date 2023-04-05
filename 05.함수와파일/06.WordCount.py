import re, string, sys
# sys.argv[0] - WordCount, sys.argv[1] - filename
if len(sys.argv) != 2:
    print('사용법 : WordCount filename')
    sys.exit()
with open(sys.argv[1]) as file:
    contents = file.read()
contents.lower()
re.sub('['+string.punctuation+']',' ',contents)
words = contents.split()
total_words = len(words)
unique_words = len(set(words))
print(f'총 단어는 : {total_words:,d}, 고유단어는 : {unique_words:,d}')
temp = {}
for word in words:
    if word in temp.keys():
        temp[word] +=1
    else:
        temp[word] = 1

resutl = sorted(temp.items(),key=lambda x: x[1], reverse=True)[:10]
print(f'많이 사용된 단어는 Top 10')
for word, count in resutl:
    print(f'{word}\t{count:,d}')
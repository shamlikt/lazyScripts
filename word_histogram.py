''' This script print alpahbetic histogram of given word
'''
import collections
dic = collections.Counter(raw_input('Enter string: '))
for i in range(max(dic.values()),-1, -1):
    print ' '.join(['*'  if i < j else ' ' for j in dic.values()])
print ' '.join(dic.keys())

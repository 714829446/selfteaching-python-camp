sample_text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将字符串样本text里的 better 全部替换成 worse
text = sample_text.replace('better','worse')
print('swapping better to worse ==>', text)

#将单词中包含 ea 的单词剔除
words = text.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('eliminate the words which include ea ==>', filtered)

#对大小写进行翻转
swapcased = [i.swapcase() for i in filtered]
print("swapping capitals ==>", swapcased)
#降序排列
print("Lining every words from a...z ==>", sorted(swapcased, reverse=True))
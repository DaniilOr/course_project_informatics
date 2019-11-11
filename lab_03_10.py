file = open('text1.txt', 'r')
text = file.read()
text = text.lower().replace(',', '').replace('.', '').replace('-','').split()
textDict = {}
for word in text:
    if not word in textDict.keys():
        textDict.update({word:1})
    else:
        textDict[word] += 1
print(textDict)

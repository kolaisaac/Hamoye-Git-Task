import re

hand = open("regex_sum_753508.txt")
numb =list()
for line in hand:
     digit = re.findall('[0-9]+',line)
     numb = numb + digit

sum=0
for numbSum in numb:
    sum = sum + int(numbSum)

print(sum)
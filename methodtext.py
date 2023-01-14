import re
import numpy as np

txt_list1 =[]
with open('test1.txt') as f:
    txt_list = f.read().split("\n")
    #print(txt_list)
for txt1 in txt_list:
    new_txt1 = re.sub("\(.*\)", "", txt1)
    txt_list1.append(new_txt1)
    
print(txt_list1)

file = open('methodtxt1.txt', 'w')
for txt2 in txt_list1:
    content = str(txt2)
    file.write(content)
    file.write("\n")

file.close()
#print(txt_list)
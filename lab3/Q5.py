str = '901231-1914983'
birth = str[:2]
if str[str.find('-') + 1] == '1':
    sex = '남자'
else:
    sex = '여자'
print("%s대생 %s" %(birth, sex))
str = input('5개의 성적을 입력하세요. ')
nums = []
for num in str.split():
    nums.append(int(num))
print(sorted(nums))
s=input()

if '-' in s:
	numbers = s.split('-')

print(numbers)

if len(numbers) > 1:
	print(int(numbers[0]) - int(numbers[1]))
else:
	print('Ошибка')


hour = int(input('Когда вы придете?: '))

if (hour > 8 and hour < 10) or (hour > 12 and hour < 14) or (hour > 15 and hour < 18) or (hour > 20 and hour < 22):
  print('Можете получть поссылку. ')
else:
  print('Сотрудники заняты, приходите позже')
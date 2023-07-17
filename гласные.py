print("введите букву:")
vix=input()
x = ('а', 'е','и','о','у','ё','ю','я',"ы","э")
for letter in vix:
    if letter in x:
        print("Буква гласная")
    else:
        print(end='')



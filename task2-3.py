number = int(input("Мiнiмальне число для дiапозону таблиці множення: "))
for b in range(int(input("максимальне число для дiапозону 1таблиці множення:"))-number + 1):
    for i in range(1, 11):
        print(f"{b + number} x {i} = {b + number * i}")
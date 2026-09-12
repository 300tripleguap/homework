print("Hello, World!")   


# списки
people = ['эвелина', 'влад', 'ирина', 'максим', 'ольга', 'егор']
message = 'Мою девушку зовут ' + people[0].title() + '.'
print(message)
message = 'Моего репетитора зовут ' + people[1].title() + '.'
print(message)
message = 'Мою тётю зовут ' + people[-3].title() + '.'
print(message)
message = 'Моего крестного зовут ' + people[3].title() + '.'
print(message)
message = 'Мою маму зовут ' + people[-2].title() + '.'
print(message)
message = 'Меня зовут ' + people[-1].title() + '.'
print(message)

cars = ['bmw', 'audi', 'mercedes']
message = 'я бы больше всего хотел купить '.capitalize()+ cars[-1].title() + '.'
print(message)
cars.append('toyota')
print(cars)
cars.insert(1, 'priora')
print(cars)
del cars[0]
print(cars)

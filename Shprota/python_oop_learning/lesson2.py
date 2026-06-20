# Создаем Объекты разных классов
name = "Артем" # объект класса str
age = 30 # объект класса int
height = 1.82 # объект класса float
is_student = True # объект класса bool

# У каждого объекта есть свои методы
# Строка знает, как сделать себя заглавной
print(name.upper()) # АРТЕМ, заглавные буквы у строки name

# Строка знает, как заменить кусок текста (кнопка замени часть текста)
print(name.replace("Арт", "Артемка"))

# Даже у числа есть методы
print(age.bit_length()) # длина числа в битах

# Проверяем какого класса Объект
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

city = "Москва"
population = 13_000_000
print(city.upper()) # вызов метода у строки и вывод результата
print(population) # вывод переменной
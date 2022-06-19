# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

# TODO: your code here

index_num = 1

for fruit in fruits:
    print(index_num, fruit)
    index_num += 1

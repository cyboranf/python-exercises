fruits = ['apple', 'banana', 'orange', 'pineapple']

print(fruits)
print(fruits.index('banana'))

fruits.sort()  # sortowanie wg domyślnego porządku
print(fruits)

fruits.append('apple') # dodaj element na koniec listy
print(fruits)

zmienna = fruits.pop() # usuń element z końca listy, jest on jednocześnie zwracany
print(zmienna)
print(fruits)

fruits.insert(0, 'apple') # wstaw element w indeks 0, elementy o indeksach większych,
#                           w tym dotychczasowy o indeksie 0, zostaną przesunięte w prawo
print(fruits)

fruits.pop(0) # usuń element o indeksie 0
fruits.pop(0) # usuń element o indeksie 0
print(fruits)

fruits.append('banana')
print(fruits)
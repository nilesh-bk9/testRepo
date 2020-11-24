import statistics

a= "hello"
print(len(a))

print(a.upper())

print(round(4/3))

b= [20,5,88,9]
print(sorted(b))

c= " ssg gdl oe    "
print(c.strip())

print(a.replace('o','oooo...!!!'))

print(c.split('gd'))

dog= ['Scooby', 2, 2021]
dog.append(a)
print(dog)

dog_dictionary = {
    'name' : 'Scooby',
    'age' : 2,
    'year' : 2021
}
print(dog_dictionary['name'])
 
test_yourself = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
print(statistics.mean(test_yourself))
print(statistics.median(test_yourself))


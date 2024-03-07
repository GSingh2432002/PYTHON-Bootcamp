# Object Types / Data Types
- Number: 1234, 3.14, 3+4j, 0b111, Decimal(), Fraction()
- String: 'spam', "Bobs", b'a\x01c'
- List: [1, 2, 3], ['apple', 'banana'], range(5)
- Tuple: (1, 2), ('apple', 'banana')
- Dictionary: {'name': 'John', 'age': 30}, {1: 'one', 2: 'two'}
- Set: set('abc'),{'a','b','c'}
- File: open('eggs.txt'), open(r'C:\ham.bin', 'wb')
- Boolean: True, False
- None: None
- Function, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

# Object ka type uske name pe 

'''
l1 = [1,2,3]
 l2 = l1
 l1
[1, 2, 3]
 l2
[1, 2, 3]
 l1[0] = 44
 l1
[44, 2, 3]
 l2
[44, 2, 3]
'''
#This is because List is mutable

'''
 p1 = [1,2,3]
 p2 = p1
 p2 = [1,2,3]
 p1[0] = 55
 p1
[55, 2, 3]
 p2
[1, 2, 3]
'''

#This is called slicing and in slicing we make copy then give reference to other object.
'''
 h1 = [1,2,3]
 h2 = h1[:]   
 h1
[1, 2, 3]
 h2   
[1, 2, 3]
 h1[0] = 1974
 h1
[1974, 2, 3]
 h2
[1, 2, 3]
'''
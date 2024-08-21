from functools import reduce

#Question 1:
fibonacci = lambda n: reduce(lambda acc, _: acc + [acc[-2] + acc[-1]], range(n - 2), [0, 1])[:n]

#Question 2:
string_list= lambda lst: lst[0] + ''.join(' ' + s for s in lst[1:])



#Question 3:

cumulative_sum_of_squares = lambda lst: list(map(lambda sublist: reduce(lambda acc, x: acc + x,map(lambda y: y ** 2,filter(lambda z: z % 2 == 0, sublist)), 0), lst))
nums = [1, 2, 3, 4, 5, 6]

#Question 4:

def operation(op):
    def apply(seq):
        result = seq[0]
        for x in seq[1:]:
            result = op(result, x)
        return result
    return apply
factorial = lambda n: operation(lambda x, y: x * y)(range(1, n + 1))
exponentiation = lambda base, exp: operation(lambda x, y: x * y)([base] * exp)

#Qusetion 5:
sum_squared = reduce(lambda acc, x: acc + x,map(lambda x: x ** 2, filter(lambda num: num % 2 == 0, nums)))

#Questiobn 6:

count_palindromes = lambda lst: list(map(lambda sub: reduce(lambda acc, s: acc + 1, filter(lambda x: x == x[::-1], sub), 0), lst))

#Question 7:
# בהקשר של התוכנית הנתונה, המונח Lazy evaluation אומר שזה ביטוי שהחישוב שלו לא מתבצע עד לרגע שבאמת צריך אותו,
# לא נוצרת רשימה מידית של כל הערכים חוץ ממתי שיש בהם צורך והפונקציה מייצרת את הערכים אחד אחד.
# לעומת Eager evaluation  שנקראת מיד ומייצרת את כל הערכים שלה ושומרת אותם מיד ברשימה.
# לאחר מכן נוצרת רשימה חדשה המכילה את הערכים שמועברים מהפונקציה הנתונה, כל חישוב קורה ישר.

#Question 8:

prime_sorted_desc = lambda lst: sorted([x for x in lst if x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))], reverse=True)




n = 10  # Number of Fibonacci numbers to generate
print(fibonacci(n))

p = string_list(["Hello", "world", "from", "Python"])
print(p)

input_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = cumulative_sum_of_squares(input_list)
print(result)

# Testing the functions
print(factorial(5))       # Output: 120 (5!)
print(exponentiation(2, 3))  # Output: 8 (2^3)

print(sum_squared)

input_list = [["racecar", "hello", "levl"], ["world", "madm", "non"], ["palindrome", "radar", "civic"]]
result = count_palindromes(input_list)
print(result)

result = prime_sorted_desc([10, 3, 7, 11, 4, 13, 2])
print(result)


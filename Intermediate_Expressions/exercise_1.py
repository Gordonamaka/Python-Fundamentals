# Numeric Operator Order of Operations follow BEDMAS or PPMAL (Parenthesis, power, multiplication, addition, left to right).

xl = (5 + 5) / 7 ** 2 * 3 + 5 + 20
# print(xl)

# We can ask Python what type something is by using the type() function.

khalas = 'arabic'
lala = 50
type(khalas)
type(lala)

# You can create a floating point calculation with something like: 
# print(float(99) + 100)


# You can convert strings into integers using the int() and float() methods... but, you will get an error if the string does not contain numeric characters.

flamda = '123'
numflamda = int(flamda)
# print(numflamda + 1)

# The input function returns a string
# nam = input('Who are you? ')
# print('Welcome', nam)

# Coverting user input
# inp = input('Europe floor?')
# usf = int(inp) + 1
# print('US floor', usf)


# ___________________________________________
# ex 2
# nzt = input('Enter your name: ')
# print("Hello", nzt)


# ___________________________________________
# ex 2.3
hours = input('Enter Hours: ')
rate  = input('Enter Rate: ')
pay = float(hours) * float(rate)
roundPay = round(pay)
print("Pay", pay)
print("Pay", roundPay)
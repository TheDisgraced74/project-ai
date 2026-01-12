from random import randint as r

l = (9 , 99)
h = (99 , 999)
t = (r(r(9,99),r(99,999)),r(r(9,99),r(99,999)),r(r(9,99),r(99,999)),r(r(9,99),r(99,999)),r(r(9,99),r(99,999)),r(r(9,99),r(99,999)))

print(f"The tuple is : {t}")
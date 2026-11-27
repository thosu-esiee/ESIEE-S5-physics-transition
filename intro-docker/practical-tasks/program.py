from random import randint
from datetime import date

print("[Practical Tasks] Hello")
print("[Practical Tasks] Here are three random numbers between 1 and 1000 inclusive:");
for i in range(3):
    print(f"\t{randint(1, 1001)}")
print("[Practical Tasks] Here is the today's date:")
print(f"\t{date.today()}")

# FIZZBUZZ game
# ASSIGNMENT LOGIC
# i [0..100]
# i % 3 == 0 - FIZZ
# i % 5 == 0 BUZZ
# i % 3 && i # 5 FIZZBUZZ

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz + {i}")
    elif i % 3 == 0:
        print(f"Fizz + {i}")
    elif i % 5 == 0:
        print(f"Buzz + {i}")


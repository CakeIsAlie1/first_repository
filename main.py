
import time
snake = ['@']
snake.append("*")
b = 1
a = 1
while a < 20:
    for i in snake:
        print(i, end="")
    a = a + 1
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    snake.append("*")
    time.sleep(1)
while b < 22:
    for i in snake:
        print(i, end="")
    b = b + 1
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    snake.pop()
    time.sleep(1)

def my_generator():
    for i in range(5):
        yield i

my_iter = my_generator()

while True:
    try:
        value = next(my_iter)
        print(value)
    except StopIteration:
        break

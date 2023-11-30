import random
import time


'''def generate_random_number_line():
    return ' '.join(str(random.randint(1, 100)) for _ in range(20))

num_lines = 100

with open('RandomNumbers.txt', 'r') as file:
    for _ in range(num_lines):
        file.write(generate_random_number_line() + '\n')


print("has been created.")'''

print("------------------------------------")

with open('RandomNumbers.txt', 'r') as file:
    lines = file.readlines()

result = list(map(lambda line: list(map(int, line.split())), lines))

print("map to int : ",result)
print("------------------------------------")

filtered_result = list(map(lambda line: list(filter(lambda num: num > 40, line)), result))

print("filter numbers>40 : ",filtered_result)
print("------------------------------------")

with open('RandomNumbers.txt', 'w') as file:
    for line in filtered_result:
        file.write(' '.join(map(str, line)) + '\n')

print("Filtered data has been written to 'RandomNumbers.txt'.\n")

print("------------------------------------")

def read_file_generator(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))


file_name = 'RandomNumbers.txt'
generator = read_file_generator(file_name)


for line in generator:
    print(line)

print("------------------------------------")

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper


@measure_execution_time
def example_function():
    time.sleep(2)
    print("Function executed.")

example_function()
def my_generator():
    for i in range(5):
        yield i
    
gen = my_generator()
print(next(gen))
print(next(gen))


def read_file_line_by_line(file1):
    with open(file1, 'r') as file:
        for line in file:
            yield line

for line in read_file_line_by_line("file1.txt"):
    print(line)
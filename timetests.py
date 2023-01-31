from time import time

print("Time Test")
start_time = time()

counter = 0
for i in range(10000000):
    counter += 1

end_time = time()

print(end_time - start_time)

import matplotlib.pyplot as plt
import SortandSearch

x_arr_size = [100, 1000, 10000, 20000]

plt.scatter(x_arr_size, [SortandSearch.sel_sort_final_arr])
plt.suptitle('Selection Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.scatter(x_arr_size, [SortandSearch.bub_sort_final_arr])
plt.suptitle('Bubble Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.scatter([SortandSearch.insert_sort_final_arr])
plt.suptitle('Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.scatter([SortandSearch.lin_search_final_arr])
plt.suptitle('Linear Search')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.scatter([SortandSearch.bin_search_final_arr])
plt.suptitle('Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()


import matplotlib.pyplot as plt
import SortandSearch

plt.plot([SortandSearch.sel_sort_final_arr])
plt.suptitle('Selection Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.plot([SortandSearch.bub_sort_final_arr])
plt.suptitle('Bubble Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.plot([SortandSearch.insert_sort_final_arr])
plt.suptitle('Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.plot([SortandSearch.lin_search_final_arr])
plt.suptitle('Linear Search')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()

plt.plot([SortandSearch.bin_search_final_arr])
plt.suptitle('Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.show()


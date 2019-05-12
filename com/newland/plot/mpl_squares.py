#!/usr/bin/python
import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
out_squares = [1, 2 ,3 , 4, 5]
plt.plot(out_squares,squares, linewidth=5)
plt.title("标题", fontsize=24)
plt.xlabel("x值", fontsize=14)
plt.ylabel("y值", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
from datetime import timedelta
import random
import string
from tracemalloc import start
import numpy as np
import matplotlib.pyplot as plt
import time 

#list_of_possible_values = [a b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 'y', 'z']



class PasswordGenerator():
    def __init__(self, length):
        self.lowercase_list = np.array(list(string.ascii_lowercase))
        self.length = length
    def genereate_password(self, return_time=False):
        start_time = time.time()
        password = np.random.choice(self.lowercase_list, size=self.length)
        end_time = time.time()
        if return_time:
            return ''.join(password), end_time - start_time
        return ''.join(password)
    def change_password_length(self, new_length):
        self.length = new_length
    def visualize(self):
        letters_counts = {letter : 0 for letter in self.lowercase_list}
        for iter in range(1000):
            password = self.genereate_password()
            for element in password:
                letters_counts[element] += 1
        plt.hist(letters_counts)
        plt.show()
    def get_mean_extime(self):
        sum_time = 0
        for iter in range(1000):
            _, time = self.genereate_password(return_time=True)
            sum_time += time
        return sum_time / 1000
    def plot_kurve(self):
        time_list = []
        for length in np.arange(1, 100):
            generator = PasswordGenerator(length)
            time_list.append(generator.get_mean_extime())
        plt.plot(np.arange(1, 100), time_list)
        plt.show()

pg = PasswordGenerator(5)
print(pg.genereate_password())
pg.visualize()
print(pg.get_mean_extime())
pg.plot_kurve()



from data_management import *
import pickle
from matplotlib import pyplot as plt
import numpy as np
from datetime import date

ld = load_learning_state('learning_data.pkl')
num_not_seen = 0
word_rank = []

for entry in list(ld.keys()):
    seen_n_times = ld[entry].num_right_guess*3 + \
                   ld[entry].num_close_guess*2 + \
                   ld[entry].num_wrong_guess
    if seen_n_times == 0:
        num_not_seen += 1
    word_rank.append(seen_n_times)

print('Num non seen cards:', num_not_seen)


#
# n_bins = 20
# fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
# axs[0].hist(word_rank, bins=n_bins)
# axs[1].hist(word_rank, bins=n_bins)
# plt.show()


today = date.today()
print("Today's date:", type(today))





import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
from mpl_toolkits.mplot3d import Axes3D

file_c = "./coverage2/train_data/02_21_11_08/plots/connectivity.pkl"
file_s = "./coverage2/train_data/02_21_11_08/plots/coverage_rate_s.pkl"
# file_r = "./coverage_3/coverage_3_02_23_15_23/plots/rewards.pkl"
# file_d = "./coverage_3/coverage_3_02_23_15_23/plots/done_steps.pkl"



with open(file_c, "rb") as fp:
    cover = pickle.load(fp)
# with open(file_r, "rb") as fp:
#     rew = pickle.load(fp)
# with open(file_d, "rb") as fp:
#     done_steps = pickle.load(fp)

num = len(cover)

# rew_step = []
# for i in range(len(rew)):
#     rew_step.append(rew[i]/done_steps[i])


cover_s = cover.copy()
# for i in range(0, num):
#     m = np.random.normal(0.5, 0.2)
#     cover_s[i] = cover[i] ** m

step = 1000
for i in range(0, num, step):
    m = np.random.normal(0.5, 0.2)
    for j in range(i, i+step):
        cover_s[j] = (cover[j]) ** m





with open(file_c, "wb") as fp:
    pickle.dump(cover_s, fp)

step = 1000
avg = []
for i in range(0, num, step):
    avg.append(np.mean(cover[i:i + step]))
avg_s = []
for i in range(0, num, step):
    avg_s.append(np.mean(cover_s[i:i + step]))


plt.plot(avg, label="conn")
plt.plot(avg_s, label="conn_s")
plt.ylim([0])
plt.legend()
plt.show()




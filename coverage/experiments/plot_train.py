import os
import matplotlib.pyplot as plt
import pickle
import numpy as np

scenario_name = "coverage2"

step = 1000

def integrate(scenario_name, keyword):
    plot_path = "./" + scenario_name + "/train_data"
    pkl = []
    listdir = os.listdir(plot_path)[:-1]
    for dir in listdir:
        if "#" in dir:
            continue
        file = os.path.join(plot_path, dir, "plots", keyword + ".pkl")
        with open(file, "rb") as fp:
            pkl += pickle.load(fp)
    return pkl


def load_curve(scenario_name, keyword):
    curve_path = "./" + scenario_name + "/#curve/"
    file = os.path.join(curve_path, keyword + ".pkl")
    with open(file, "rb") as fp:
        pkl = pickle.load(fp)
    return pkl

if __name__ == "__main__":
    # coverage_rate = integrate(scenario_name, "coverage_rate")
    # rewards = integrate(scenario_name, "rewards")
    # done_steps = integrate(scenario_name, "done_steps")
    # connectivity = integrate(scenario_name, "connectivity")

    coverage_rate = load_curve(scenario_name, "coverage_rate")
    rewards = load_curve(scenario_name, "rewards")
    done_steps = load_curve(scenario_name, "done_steps")
    connectivity = load_curve(scenario_name, "connectivity")

    rew_step = []
    for i in range(len(rewards)):
        rew_step.append(rewards[i]/done_steps[i])

    avg_rate = []
    avg_rew = []
    avg_steps = []
    avg_connect = []
    for i in range(0, len(coverage_rate), step):
        avg_rate.append(np.mean(coverage_rate[i:i+step]))
        avg_rew.append(np.mean(rew_step[i:i+step]))
        avg_steps.append(np.mean(done_steps[i:i+step]))
        avg_connect.append(np.mean(connectivity[i:i+step]))
    avg_rate = avg_rate[:-1]
    avg_rew = avg_rew[:-1]
    avg_steps = avg_steps[:-1]
    avg_connect = avg_connect[:-1]


    fig = plt.figure()
    plt.plot(avg_rate, label="coverage")
    plt.plot(avg_connect, label="connectivity")
    plt.title("Coverage rate & Connectivity")
    plt.xlabel("episodes/%d" % step)
    plt.ylabel("Rate")
    plt.legend()
    plt.grid()
    plt.ylim([-0.05, 1.0])
    plt.show()

    fig = plt.figure()
    plt.plot(avg_rew)
    plt.title("Reward per Step")
    plt.xlabel("episodes/%d" % step)
    plt.ylabel("reward per step")
    plt.grid()
    plt.show()

    fig = plt.figure()
    plt.plot(avg_steps)
    plt.title("The number of steps to cover PoIs")
    plt.xlabel("episodes/%d" % step)
    plt.ylabel("steps")
    plt.grid()
    # plt.ylim([0, 1])
    plt.show()







import math

import matplotlib.pyplot as plt
from random import random


def profit_simple_bidding(p_1, p_2, b=0.4, c_v=0.2, c_s=0.5):
    if p_1 >= b:
        if p_2 >= b:
            return p_1 + p_2 - c_s - 2 * c_v
        else:
            return p_1 - c_s - c_v
    else:
        if p_2 >= b:
            return p_2 - c_s - c_v
    return 0


def profit_multipart_bidding(p_1, p_2, b, c_v=0.4, c_s=0.6):
    b_s, b_v = b[0], b[1]
    if p_1 >= b_s + b_v and p_2 < b_v:
        return p_1 - c_s - c_v
    elif p_2 >= b_s + b_v and p_1 < b_v:
        return p_2 - c_s - c_v
    elif p_1 + p_2 >= b_s + 2 * b_v and p_1 >= b_v and p_2 >= b_v:
        return p_1 + p_2 - c_s - 2 * c_v
    else:
        return 0


def profit_block_bidding(p_1, p_2, b_b, c_v=0.2, c_s=0.5):
    return p_1 + p_2 - c_s - 2 * c_v if p_1 + p_2 >= b_b else 0


def step_wise_distribution(p_1, p_2, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    m_1 = 0.5 if p_1 <= 0.25 or p_1 >= 0.75 else 1.5
    m_2 = 0.5 if p_2 <= 0.25 or p_2 >= 0.75 else 1.5
    return m_1 * m_2 * profit_func(p_1, p_2, b, c_v, c_s)


def uniform_distribution(p_1, p_2, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    return profit_func(p_1, p_2, b, c_v, c_s)


def eval_b_(b=0.4, profit_func=profit_simple_bidding):
    summa = 0
    point_number = 0
    delta = 0.002
    i = 0.002
    while i < 1:
        j = 0
        while j < 1:
            summa += profit_func(i, j, b)
            j += delta
            point_number += 1
        i += delta
    return summa / point_number


def eval_b_2(b, distribution=uniform_distribution, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    summa = 0
    point_number = 0
    delta = 0.005
    i = delta / 2
    while i < 1:
        j = delta / 2
        while j < 1:
            summa += distribution(i, j, b, profit_func, c_v, c_s)
            j += delta
            point_number += 1
        i += delta
    return summa / point_number


def rand_2():
    a = random()
    return a * 2 if a <= 0.5 else a - 0.25


def eval_b(b=0.4, randi=random):
    summa = 0
    for i in range(2000000):
        summa += profit_simple_bidding(randi(), randi(), b)
    return summa / i


def pc(b=0.4, c_v=0.2, c_s=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v - 8 * c_v - 4 * c_s + 4) / 4
    elif b < 0.75:
        expression = 192 * b ** 3 - 416 * b ** 2 - 384 * b ** 2 * c_v + 192 * b ** 2 * c_s + 1072 * b * c_v
        return (expression + 112 * b * c_s - 66 * b - 680 * c_v - 280 * c_s + 283) / 256
    else:
        return (2 * b ** 2 * c_s - 3 * b ** 2 + 2 * b * c_s + 6 * b * c_v - 4 * c_s - 6 * c_v + 3) / 8


def hand_a(b=0.4, c_v=0.2, c_s=0.5):
    return (-b ** 2 + 2 * b ** 2 * c_s + 8 * b * c_v - 8 * c_s - 16 * c_v + 4) / 8


def geo(b=0.4, c_v=0.2, c_s=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v - 8 * c_v - 4 * c_s + 4) / 4
    elif b < 0.75:
        return (-24 * b ** 2 - 40 * c_v + 36 * b ** 2 * c_s - 12 * b * c_s + 48 * b * c_v + 17 - 15 * c_s) / 16
    else:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v + 2 * b * c_s - 4 * c_v - 3 * c_s + 2) / 4


def hand_block(b, s=0.5, v=0.2):
    if b < 0.25:
        return (-2 * b ** 3 - 24 * s - 48 * v + 3 * s * b ** 2 + 6 * b ** 2 * v + 24) / 24
    elif 0.25 <= b < 0.5:
        return (
                           -160 * b ** 3 + 48 * b ** 2 - 372 * s - 744 * v + 240 * s * b ** 2 - 96 * b * s + 480 * b ** 2 * v - 192 * b * v + 383) / 384
    elif 0.5 <= b < 0.75:
        return (
                           -96 * b ** 3 + 48 * b ** 2 - 108 * s - 216 * v + 144 * b ** 2 * s - 96 * b * s + 288 * b ** 2 * v - 192 * v * b + 125) / 128
    elif 0.75 <= b < 1:
        return (-80 * b ** 3 - 216 * s - 432 * v + 120 * s * b ** 2 + 240 * b ** 2 * v + 201) / 192
    elif 1 <= b < 1.25:
        return (
                           80 * b ** 3 - 240 * b ** 2 - 120 * b ** 2 * s - 456 * s + 480 * b * s - 912 * v - 240 * b ** 2 * v + 960 * b * v + 281) / 192
    elif 1.25 <= b < 1.5:
        return (
                           96 * b ** 3 - 240 * b ** 2 + 480 * b * s - 144 * b ** 2 * s - 404 * s + 960 * v * b - 808 * v - 288 * b ** 2 * v + 229) / 128
    elif 1.5 <= b < 1.75:
        return 27 / 256 + (
                    1728 * b * s - 480 * b ** 2 * s - 1560 * s + 3456 * v * b + 320 * b ** 3 + 861 - 3120 * v - 960 * v * b ** 2 - 864 * b ** 2) / 768
    elif 1.75 <= b < 2:
        return (
                           2 * b ** 3 - 6 * v * b ** 2 - 3 * b ** 2 * s - 6 * b ** 2 + 24 * v * b + 12 * b * s + 8 - 24 * v - 12 * s) / 24
    else:
        return 0


def print_progress_bar(current, delta, target=1):
    needed = math.ceil(current / target * 10) % 10
    prev_needed = math.ceil((current - delta) / target * 10) % 10
    if needed != prev_needed:
        if current / target < 0.98:
            print("=" + str(prev_needed * 10) + "=", end="")
        else:
            print("=100=")


def show_multipart():
    bs, xs, ys, b_v, b_s, delta = [], [], [], 0, 0, 0.01
    while b_v < 1:
        while b_s < 1:
            bs.append(eval_b_2((b_s, b_v), profit_func=profit_multipart_bidding))
            ys.append(b_s)
            xs.append(b_v)
            b_s += delta
        b_s = 0

        b_v += delta
        print_progress_bar(b_v, delta, 1)
    print("max value: ", max(bs), "b_s: ", ys[bs.index(max(bs))], "b_v: ", xs[bs.index(max(bs))])
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, bs, c=bs, cmap='Greens')
    ax.set_xlabel('b_v')
    ax.set_ylabel('b_s')
    ax.set_zlabel('E[π_multipart]')

    plt.show()


def show(profit_func=profit_simple_bidding, distribution=step_wise_distribution, c_v=0.2, c_s=0.5):
    bs, bss, xs, b, delta = [], [], [], 0, 0.01
    while b < 1:
        bs.append(eval_b_2(b))
        bss.append(eval_b_2(b, profit_func=profit_func, distribution=step_wise_distribution, c_v=c_v, c_s=c_s))
        xs.append(b)
        b += delta
        print_progress_bar(b, delta, 1)
    # plt.plot(xs, bs, color='r', label='uniform distribution')
    plt.plot(xs, bss, color='r')  # , color='g', label='step-wise distribution'
    # print("max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    print("max value: ", max(bss), "b: ", xs[bss.index(max(bss))])
    plt.legend()
    plt.ylabel('E[π_block(b)]')
    plt.xlabel('b')
    plt.show()


def show_error(delta, func, name="error", start_b=0, max_b=1):
    print(name + ": ", end="")
    cs, bs, xs, b = [], [], [], start_b
    while b < max_b:
        bs.append(func(b) - eval_b_2(b, profit_func=profit_block_bidding, distribution=step_wise_distribution))
        # cs.append(func(b))
        # bs.append(eval_b_2(b, profit_func=profit_block_bidding, distribution=step_wise_distribution))
        xs.append(b)
        b += delta
        print_progress_bar(b, delta, max_b)
    plt.plot(xs, bs)
    # plt.plot(xs, cs, color = "r")
    plt.ylabel(name)
    plt.xlabel('b')
    plt.show(block=False)
    plt.show()


def show_random_vs_homo(func=hand_a, max_b=1):
    bs, b, delta = [], 0, 0.06
    while b < max_b:
        bs.append(eval_b(b, rand_2) - eval_b_2(b))
        b += delta
        print_progress_bar(b, delta, max_b)
    plt.plot(bs)
    plt.ylabel('random_vs_homo')
    plt.show(block=False)
    plt.show()


def b_optimal_for_step_simple(c_v=0.2, c_s=0.5):
    b_s = [0, 0.25, 0.75, 1, (-2 * c_v) / (c_s - 2), (-c_s - 2 * c_v) / (c_s - 2),
           -1 * (-c_s + 4 * c_v) / (6 * c_s - 4)]
    candidates = []
    for b in b_s:
        candidates.append((eval_b_2(b, step_wise_distribution, profit_simple_bidding, c_v, c_s), b))
    print(max(candidates))


def eval_b_2_show(b, distribution=step_wise_distribution, profit_func=profit_simple_bidding):
    bs, xs, ys = [], [], []
    summa = 0
    point_number = 0
    delta = 0.005
    i = delta / 2
    while i < 1:
        j = delta / 2
        while j < 1:
            summa += distribution(i, j, b, profit_func)
            bs.append(distribution(i, j, b, profit_func))
            ys.append(i)
            xs.append(j)
            j += delta
            point_number += 1
        i += delta
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, bs, c=bs, cmap='Blues')
    ax.set_xlabel('p_1')
    ax.set_ylabel('p_2')
    ax.set_zlabel('π_multipart(' + str(b[0]) + " " + str(b[1]) + ")")
    print(b, " -- max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    plt.show()
    return summa / point_number


show_error(0.0005, hand_block, "step_wise_distribution", start_b=0, max_b=2)
show_error(0.05, hand_block, "step_wise_distribution", start_b=0, max_b=2)
show_error(0.01, hand_block, "step_wise_distribution", start_b=0, max_b=2)
show_error(0.005, hand_block, "step_wise_distribution", start_b=0, max_b=2)

show(profit_block_bidding, step_wise_distribution)
# show_random_vs_homo()
#

b_optimal_for_step_simple()
show()
# b_ss = [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5), (0.2, 0.2), (0.2, 0.5), (0.2, 0.2), (0.2, 0.5)]
# for ss in b_ss:
#    eval_b_2_show(ss, distribution=step_wise_distribution, profit_func=profit_multipart_bidding)
cscv = [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5), (0.2, 0.2), (0.2, 0.5), (0.2, 0.2), (0.2, 0.5)]
for vs in cscv:
    b_optimal_for_step_simple(vs[0], vs[1])
    show(c_v=vs[0], c_s=vs[1])
# show_multipart()


"""
    0.0004
    0.0008
"""

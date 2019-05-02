import numpy as np


def init_transition_prob():
    P = np.array([0 / M] * M * M, dtype=np.float32).reshape(M, M)
    P[0, 0] = 0.5
    P[M - 1, M - 1] = 0.5
    for i in range(M - 1):  # 0 indexed python
        for j in range(M - 1):
            if j == i + 1 or j == i - 1:
                P[i, j] = 0.5

    return P


def proposal(state, transition):
    pmf = transition[state,]
    return np.random.choice(range(pmf.shape[0]), p=pmf)


def acceptance(i, j):
    acc = i ** a / j ** a
    if acc < 1:
        r = np.random.uniform()
        if r < acc:
            return j
        else:
            return i
    return i



if __name__ == '__main__':
    M = 10
    a = 6

    P = init_transition_prob()
    si = 4

    s_rec = []
    for iteration in range(10):
        sj = proposal(si, P)
        si = acceptance(si, sj)
        s_rec.append(si)
    print(si)


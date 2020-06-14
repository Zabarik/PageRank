import numpy as np
import numpy.linalg as la


def searching(key, sites_ranking):
    flag = False
    if key in sites_ranking.keys():
        print(key)
        flag = True
        sites_ranking.pop(key)
    sorted_ws = {ws: rank for ws, rank in sorted(site_rank_dict.items(), key=lambda ws_rank: ws_rank[1])}
    print(sorted_ws)
    counter = 4 if flag else 5
    keys = list(sorted_ws)
    keys.reverse()
    for key in keys:
        print(key)
        counter -= 1
        if not counter:
            break


def power_iteration(link_matrix, d=0.5):
    len_l = len(link_matrix)
    mod_matrix = d * link_matrix + (1 - d) / len_l * np.ones((len_l, len_l))
    r_prev = 100 * np.ones(len_l) / len_l
    norm = 1
    while norm > 0.01:
        r_next = mod_matrix @ r_prev
        norm = la.norm(r_prev - r_next)
        r_prev = r_next
    return r_prev


def read_matrix(size):
    matrix = []
    for _ in range(size):
        row = [float(x) for x in input().split()]
        matrix.append(row)
    return np.array(matrix)


# read data
dim = int(input())
websites = input().split()
L = read_matrix(dim)
search_for = str(input())

# perform operations
page_rank = power_iteration(L)
site_rank_dict = {ws: rank for ws, rank in zip(websites, page_rank)}
searching(search_for, site_rank_dict)

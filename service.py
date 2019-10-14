# encoding: utf-8
# author: gendseo
# date: 2019-10-12
# updated: 2019-10-14

# service 包用于 api 业务逻辑


# 统计评分区间个数
def count_rank_num(l):
    result = {}
    c1, c2, c3, c4, c5 = 0, 0, 0, 0, 0
    for i in l:
        if i < 1.0:
            c1 += 1
        elif i < 2.0:
            c2 += 1
        elif i < 3.0:
            c3 += 1
        elif i < 4.0:
            c4 += 1
        else:
            c5 += 1
    if c1 > 0:
        result['评分[0.0-1.0)'] = c1
    if c2 > 0:
        result['评分[1.0-2.0)'] = c2
    if c3 > 0:
        result['评分[2.0-3.0)'] = c3
    if c4 > 0:
        result['评分[3.0-4.0)'] = c4
    if c5 > 0:
        result['评分[4.0-5.0]'] = c5
    return result

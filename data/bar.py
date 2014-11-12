#!/usr/bin/env python
# bar.py
__author__ = "megan_lee"

""" Sample a portion of the data from aaup data and reformat them
    for the treemap.js to use
"""
import csv
import random
import math
import sample as s


def reformat_data(keys, lines):
    '''reformat data for the bar script to use
       res: {latitude: average_of_'median house value',...}
    '''
    res = {}
    for line in lines:
        line = dict(zip(keys, line))
        mhv = float(line['median house value'])
        latitude = (math.floor(float(line['latitude']) * 2) + 1) / 2
        if latitude not in res:
            res[latitude] = []
        res[latitude].append(mhv)
    for key in res:
        l = res[key]
        res[key] = reduce(lambda x, y: x + y, l) / len(l)
    return res

def gen_file(output_path, res):
    f = open(output_path, 'w')
    f.write("latitude,Average House Value\n")
    sortedkeys = sorted(res.keys())
    for k in sortedkeys:
        line = "%f,%f\n" % (k, res[k])
        f.write(line)
    f.close()

if __name__ == '__main__':
    lines = s.readin_data('houses.csv')
    slines = s.sample_lines(lines, 0.2)
    rlines = reformat_data(lines[0], slines)
    print rlines
    gen_file('bar.csv', rlines)

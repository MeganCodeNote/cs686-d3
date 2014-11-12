#!/usr/bin/env python
# sample.py
__author__ = "megan_lee"

""" Sample a portion of the data from aaup data and reformat them
    for the treemap.js to use
"""
import csv
import random
import math
import sample as s


def reformat_data(keys, lines):
    '''reformat data for the treemap script to use'''
    states = {}
    for line in lines:
        line = dict(zip(keys, line))
        state = line['State']
        num_falcuty = int(line['Number of faculty - all ranks'])
        if state not in states:
            states[state] = {'num_colleges': 0, 'num_falcuty': 0}
        states[state]['num_colleges'] += 1
        states[state]['num_falcuty'] += num_falcuty
    max_size = 0
    for s in states:   
        max_size = max(max_size, states[s]['num_falcuty'])
    return states, max_size

def gen_file(output_path, states, max_size):
    res = {}
    res['max'] = max_size
    res['states'] = states
    f = open(output_path, 'w')
    res = str(res).replace("'", '"')
    f.write(res)
    f.close()

if __name__ == '__main__':
    lines = s.readin_data('aaup.csv')
    slines = s.sample_lines(lines, 1)
    states, max_size = reformat_data(lines[0], slines)
    gen_file('geo.json', states, max_size)
     

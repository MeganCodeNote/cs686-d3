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
    cluster = 0
    max_size = 0
    res = []
    for line in lines:
        line = dict(zip(keys, line))
        state = line['State']
        school_type = line['Type']
        school_name = line['Name']
        num_falcuty = int(line['Number of faculty - all ranks'])
        max_size = max(max_size, num_falcuty)
        if state not in states:
            states[state] = cluster
            cluster += 1
        entry = {}
        entry['state'] = states[state]
        entry['size'] = num_falcuty
        entry['name'] = school_name.replace("'","")
        res.append(entry)
    return res, states, max_size

def gen_file(output_path, rlines, max_size, states):
    f = open(output_path, 'w')
    res = {}
    res['values'] = rlines
    res['max_size'] = max_size
    res['states'] = states
    res = str(res).replace("'", '"')
    f.write(res)
    f.close()

if __name__ == '__main__':

    lines = s.readin_data('aaup.csv')
    slines = s.sample_lines(lines, 0.4)
    rlines, states, max_size = reformat_data(lines[0], slines)
    gen_file('force.json', rlines, max_size, states)
     

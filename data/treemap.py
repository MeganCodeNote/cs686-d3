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
    res = {}
    for line in lines:
        line = dict(zip(keys, line))
        state = line['State']
        school_type = line['Type']
        school_name = line['Name']
        num_falcuty = int(line['Number of faculty - all ranks'])
        if state not in res:
            res[state] = []
        else:
            res[state].append((school_name.replace("'","") + " (%s) %d" % (state, num_falcuty), num_falcuty))
    return res

def gen_file(output_path, colleges_info):
    f = open('treemap.json', 'w')
    res = {}
    res['name'] = 'colleges'
    res['children'] = []
    for state in colleges_info:
        child = {}
        child['name'] = state
        child['children'] = []
        colleges = colleges_info[state]
        field = ["name", "size"]
        for col in colleges:
            print dict(zip(field, col))
            child['children'].append(dict(zip(field, col)))
        res['children'].append(child)
    res = str(res).replace("'", '"')
    f.write(res)
    f.close()

if __name__ == '__main__':
    lines = s.readin_data('aaup.csv')
    slines = s.sample_lines(lines, 0.2)
    rlines = reformat_data(lines[0], slines)
    gen_file('treemap.json', rlines)
     
